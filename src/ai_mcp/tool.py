import platform
import psutil
import subprocess
import json

def get_host_info() -> str:
    """get host information

    Returns:
        str: the host information in JSON string
    """
    print("🔧 get_host_info tool被调用了！")
    info: dict[str, str] = {
        "system": platform.system(),
        "release": platform.release(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "memory_gb": str(round(psutil.virtual_memory().total / 1024 ** 3, 2)),
    }
    
    cpu_count = psutil.cpu_count(logical=True)
    if cpu_count is None:
        info["cpu_count"] = "unknown"
    else:
        info["cpu_count"] = str(cpu_count)
    

    try:
        cpu_model = subprocess.check_output(["sysctl", "-n", "machdep.cpu.brand_string"]).decode().strip()
        info["cpu_model"] = cpu_model 
    except:
        cpu_model = "unknown"
    info["cpu_model"] = cpu_model

    return json.dumps(info, indent=4)

if __name__ == "__main__":
    print(get_host_info())
