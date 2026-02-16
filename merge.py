import os
import sys
import subprocess

def get_base_path():
    """获取程序运行时的实际目录 (兼容 PyInstaller 打包)"""
    if getattr(sys, 'frozen', False):
        # 如果是打包后的 exe，返回 exe 所在的实际文件夹
        return os.path.dirname(sys.executable)
    else:
        # 如果是 python 脚本运行，返回脚本所在文件夹
        return os.path.dirname(os.path.abspath(__file__))

# 这里的路径会自动指向和你 exe 同目录下的 ffmpeg.exe
CURRENT_DIR = get_base_path()
FFMPEG_EXE = os.path.join(CURRENT_DIR, "ffmpeg.exe")

def clean_path(path):
    """清除拖拽文件时可能产生的引号和前后空格"""
    return path.strip().strip('"').strip("'")

def merge_video_audio():
    print("\n" + "="*60)
    print("  Video & Audio Merger / 映像と音声の合成 (v3.0)")
    print("  Ready for Python 3.12 & EXE Packaging")
    print("="*60 + "\n")

    # 1. 检查 ffmpeg.exe 是否存在
    if not os.path.exists(FFMPEG_EXE):
        print(f"? ERROR / エラー:")
        print(f"  ffmpeg.exe not found in: {CURRENT_DIR}")
        print(f"  Please put 'ffmpeg.exe' in the same folder as this program.")
        print(f"  'ffmpeg.exe' をこのプログラムと同じフォルダに置いてください。")
        input("\nPress Enter to exit... / Enterを押して終了...")
        return

    # 2. 输入视频 / Video Input
    print("Please drag and drop the VIDEO file (.mp4, .webm):")
    print("映像ファイル (.mp4, .webm) をドラッグ＆ドロップしてください:")
    video_path = clean_path(input(">> "))

    # 3. 输入音频 / Audio Input
    print("\nPlease drag and drop the AUDIO file (.m4a, .weba):")
    print("音声ファイル (.m4a, .weba) をドラッグ＆ドロップしてください:")
    audio_path = clean_path(input(">> "))

    # 4. 设置输出路径 (保存在当前目录下)
    # 提取视频文件名作为前缀
    base_filename = os.path.basename(video_path).rsplit('.', 1)[0]
    output_filename = f"{base_filename}_merged.mp4"
    output_path = os.path.join(CURRENT_DIR, output_filename)

    # 5. 使用 subprocess 调用 ffmpeg 进行合成
    # -y: 覆盖已存在文件
    # -c:v copy: 视频流直接拷贝（不重新编码，极快且无损）
    # -c:a aac: 音频转码为通用 AAC 格式
    cmd = [
        FFMPEG_EXE, "-y",
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy",
        "-c:a", "aac",
        "-strict", "experimental",
        output_path
    ]

    try:
        print("\n" + "-"*30)
        print("[Processing... / 処理中...]")
        print("-"*30 + "\n")
        
        # 执行命令
        subprocess.run(cmd, check=True)
        
        print("\n" + "="*60)
        print("? SUCCESS! / 成功しました！")
        print(f"  Saved to: {output_path}")
        print("="*60)

    except Exception as e:
        print(f"\n? [ERROR / エラー]: {e}")

    input("\nPress Enter to exit... / Enterを押して終了...")

if __name__ == "__main__":
    merge_video_audio()
