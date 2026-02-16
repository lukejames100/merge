# merge
English: A high-speed, zero-dependency Python tool to merge YouTube Video (MP4/WebM) and Audio (M4A/WebA) files using FFmpeg. Supports drag-and-drop &amp; Python 3.12+. 日本語: FFmpegを使用してYouTubeの映像と音声を高速に合成するPythonツール。ドラッグ&amp;ドロップ対応、Python 3.12最適化済み。

# YouTube Video & Audio Merger (FFmpeg-based)
### 映像と音声の合成ツール (FFmpegベース)

A simple, lightweight Python tool to merge YouTube video-only files (MP4/WebM) with audio-only files (M4A/WebA). Designed for Python 3.12+ and supports drag-and-drop.

YouTubeからダウンロードした無音動画（MP4/WebM）と音声ファイル（M4A/WebA）を素早く合成する、軽量なPythonツールです。Python 3.12以降に対応し、ドラッグ＆ドロップ操作をサポートしています。

---

## ✨ Features / 特徴

* **Fast Merging**: Uses stream copying (`-c:v copy`), meaning no quality loss and near-instant processing.
    * **高速合成**: ストリームコピー（`-c:v copy`）を使用するため、画質の劣化がなく、一瞬で処理が完了します。
* **Format Support**: Works with `.mp4`, `.webm`, `.m4a`, `.weba`.
    * **対応フォーマット**: `.mp4`, `.webm`, `.m4a`, `.weba` に対応。
* **User Friendly**: Bilingual interface (English/Japanese) and drag-and-drop support.
    * **ユーザーフレンドリー**: 英語と日本語のバイリンガル表示、ドラッグ＆ドロップ操作に対応。
* **EXE Compatible**: Ready to be packaged with PyInstaller.
    * **EXE対応**: PyInstallerによる実行ファイル化が可能です。

---

## 🚀 How to Use / 使い方

### Method 1: Running with Python / Pythonで実行する場合

1.  **Download FFmpeg**: Download `ffmpeg.exe` and place it in the same directory as `merge.py`.
    * **FFmpegの準備**: `ffmpeg.exe` をダウンロードし、`merge.py` と同じフォルダに配置してください。
2.  **Run the script / 実行**:
    ```bash
    python merge.py
    ```
3.  **Drag & Drop**: Drag your video file into the window, press Enter, then drag your audio file and press Enter.
    * **操作**: 映像ファイルをウィンドウにドラッグしてEnter、次に音声ファイルをドラッグしてEnterを押すだけです。

### Method 2: Create an EXE / EXEファイルを作成する場合
![螢幕擷取畫面 2026-02-17 004819](https://github.com/user-attachments/assets/6403bd0a-bf78-462a-b86b-4ab676d4e5aa)



If you want to create a standalone executable:
実行ファイルを作成するには、以下のコマンドを使用します：

```bash
pip install pyinstaller
pyinstaller --onefile --console merge.py
