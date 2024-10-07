import os
from moviepy.editor import VideoFileClip
import tkinter as tk
from tkinter import filedialog, messagebox

class VideoToAudioConverter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Video to Audio Converter")
        self.root.geometry("400x200")
        self.setup_ui()

    def setup_ui(self):
        # Create and pack widgets
        title_label = tk.Label(self.root, text="MP4 to MP3 Converter", font=("Arial", 16))
        title_label.pack(pady=10)

        select_button = tk.Button(self.root, text="Select MP4 File", command=self.process_video)
        select_button.pack(pady=20)

        self.status_label = tk.Label(self.root, text="", wraplength=350)
        self.status_label.pack(pady=10)

    def process_video(self):
        # Get input video file
        input_file = filedialog.askopenfilename(
            filetypes=[("MP4 files", "*.mp4")],
            title="Choose a video file"
        )
        
        if not input_file:
            return

        try:
            # Update status
            self.status_label.config(text="Converting video...")
            self.root.update()

            # Convert video to audio
            video = VideoFileClip(input_file)
            
            # Extract audio
            audio = video.audio
            
            # Determine output filename
            output_file = os.path.splitext(input_file)[0] + ".mp3"
            
            # Convert audio to MP3
            audio.write_audiofile(output_file)
            
            # Close video file
            video.close()
            
            # Update status
            self.status_label.config(text=f"Conversion complete!\nSaved as: {os.path.basename(output_file)}")
            messagebox.showinfo("Success", "Audio extraction completed successfully!")
            
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def run(self):
        self.root.mainloop()

def main():
    app = VideoToAudioConverter()
    app.run()

if __name__ == "__main__":
    main()
