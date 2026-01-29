import psutil

cpu_usage = psutil.cpu_percent()
memory = psutil.virtual_memory().percent

print("CPU Usage:", cpu_usage, "%")
print("Memory Usage:", memory, "%")
