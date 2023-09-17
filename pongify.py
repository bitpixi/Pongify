from moviepy.editor import *

def pingpong_video(input_path, output_path, duration=60):
    """
    This function takes a video and extends its length by playing it forward and backward alternately.

    :param input_path: Path to the input video (MP4, MOV, or GIF).
    :param output_path: Path to save the output video.
    :param duration: Desired length for the output video in seconds. Default is 60 seconds.
    """
    # Load the video
    clip = VideoFileClip(input_path)
    
    # Check the clip's duration
    if clip.duration >= duration:
        raise ValueError("The input video's duration is longer than or equal to the desired output duration.")
    
    # Create a pingpong clip (playing forward then backward)
    pingpong_clip = clip.fx(vfx.time_mirror)
    
    # Concatenate the video to reach the desired length
    final_clip = concatenate_videoclips([pingpong_clip] * (duration // int(2*clip.duration)))
    
    # Write the result to a file
    final_clip.write_videofile(output_path, codec="libx264")
    
    # Write the result to a file
    final_clip.write_videofile(output_path, codec="libx264")

# Example usage:
# pingpong_video("input_video.mp4", "output_video.mp4")
