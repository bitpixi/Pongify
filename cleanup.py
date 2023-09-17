import os
import time

def cleanup_old_files(directory='processed', max_age_seconds=3600):
    """
    Delete files older than a specified age (in seconds) from a directory.

    :param directory: Directory to cleanup.
    :param max_age_seconds: Age (in seconds) to consider a file "old".
    """
    current_time = time.time()
    
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        file_age = current_time - os.path.getmtime(filepath)
        
        if file_age > max_age_seconds:
            os.remove(filepath)
            print(f"Deleted {filename} as it was {file_age} seconds old.")

# Call the function when the script is run
cleanup_old_files()
