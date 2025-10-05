# importing needed libraries
import psutil     
import time 

# set a cpu usage limit (in percentage)
limit = 80

# starting message
print("Monitoring CPU usage...")

try:
    # this loop will keep running until user stops it
    while True:
        # get the current cpu usage for 1 second
        usage = psutil.cpu_percent(interval=1)

        # check if usage is higher than our limit
        if usage > limit:
            print("Alert! CPU usage exceeds threshold:", usage, "%")
        else:
            print("CPU usage is normal:", usage, "%")

        # wait for 1 second before checking again
        time.sleep(1)

# this runs when user stops the program using ctrl + c
except KeyboardInterrupt:
    print("Monitoring stopped by user")

# this will handle any other unexpected error
except Exception as error:
    print("An error occurred:", error)
