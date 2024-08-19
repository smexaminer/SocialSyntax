import ffmpeg
import config


def trim_video(input_video, start_time, duration, output, quality="regular"):
    """
    Trims a video to a specified length from a given start time.
    :param input_video: Full path to video to trim.
    :param quality: The desired quality of the output video ('high', 'regular').
    :param start_time: The start time in the video to begin trimming (format: 'HH:MM:SS' or seconds).
    :param duration: The duration of the clip to trim out (in seconds).
    :param output: The path to save the trimmed video clip.
    """

    # Define scale based on quality
    if quality == "high":
        scale_width, scale_height = 1920, 1080
        video_bitrate = "5000k"  # Example high bitrate
    else:
        scale_width, scale_height = 1280, 720
        video_bitrate = "1500k"  # Example regular bitrate

    print(f"Trimming video from {start_time} for {duration} seconds in {quality} at width {scale_width} x height {scale_height}")

    try:
        (
            ffmpeg.input(input_video, ss=start_time, t=duration)
            .filter("scale", scale_width, scale_height)
            .output(
                output,
                vcodec="libx264",
                video_bitrate=video_bitrate,
                crf=18,
                pix_fmt="yuv420p",
                acodec="aac"
            )
            .overwrite_output()  # Automatically overwrite output file
            .run(capture_stdout=True, capture_stderr=True)
        )
    except ffmpeg.Error as e:
        # Print the full error message from FFmpeg
        print(f"FFmpeg error:\n{e.stderr.decode()}")
        raise  # Re-raise the error to maintain the traceback

    return output


if __name__ == "__main__":
    # Example usage:
    trim_video(
        input_video=f"{config.ASSETS_DIR}/videos/input.mp4",
        start_time="00:00:00",
        duration=5,
        output=f"{config.ASSETS_DIR}/videos/trimmed.mp4",
        quality="regular"
    )
