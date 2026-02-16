# YouTube Video & Audio Merger (One-Click EXE)
### 映像と音声の合成ツール (実行ファイル版)

A simple, ultra-fast tool to merge YouTube Video-only files (MP4/WebM) and Audio-only files (M4A/WebA) into a single high-quality MP4. No Python installation required!

YouTubeからダウンロードした映像（MP4/WebM）と音声（M4A/WebA）を、画質劣化なしで素早く合成するツールです。Pythonのインストールは不要で、すぐにお使いいただけます。

---

## 📥 Download / ダウンロード

You can download the ready-to-use executable files from Google Drive:
以下のGoogleドライブリンクから、すぐに使える実行ファイルをダウンロードしてください：

👉 **[Download from Google Drive / Googleドライブからダウンロード](https://drive.google.com/drive/folders/1Grikl0DZ3pECZwAfqem8g_NOlogPDVbV?usp=drive_link)**

> **Note**: Please download both `merge.exe` and `ffmpeg.exe`.
> **注意**: `merge.exe` と `ffmpeg.exe` の両方をダウンロードしてください。

---

## 🚀 How to Use / 使い方

1.  **Place Files**: Put `merge.exe` and `ffmpeg.exe` in the same folder.
    * **準備**: `merge.exe` と `ffmpeg.exe` を同じフォルダに置きます。
2.  **Run**: Double-click `merge.exe`.
    * **実行**: `merge.exe` をダブルクリックして起動します。
3.  **Drag & Drop**: 
    * When prompted, drag your **Video file** into the window and press **Enter**.
    * Then, drag your **Audio file** into the window and press **Enter**.
    * **操作**: 
        * 指示に従って**映像ファイル**をウィンドウにドラッグし、**Enter**を押します。
        * 次に**音声ファイル**をドラッグし、**Enter**を押します。
4.  **Done**: The merged file `*_merged.mp4` will be created in the same folder instantly.
    * **完了**: 合成されたファイル `*_merged.mp4` が同じフォルダ内に一瞬で生成されます。

---

## ✨ Features / 特徴

* **No Installation**: Runs directly on Windows.
    * **インストール不要**: Windows上でそのまま動作します。
* **Zero Quality Loss**: Uses stream-copy technology to ensure original quality.
    * **画質劣化なし**: ストリームコピー技術により、元の画質を完全に維持します。
* **Fast Processing**: Completes merging in seconds.
    * **超高速**: 数秒で合成が完了します。
* **Format Support**: MP4, WebM, M4A, WebA.
    * **対応フォーマット**: YouTubeの主要な形式をすべてサポート。

---

## 🛠 Prerequisites / 必要条件

* Windows OS
* `ffmpeg.exe` must be in the same directory as `merge.exe`.
* `ffmpeg.exe` は必ず `merge.exe` と同じディレクトリに置いてください。

---

## 📝 License / ライセンス

MIT License. Free to use and distribute.
MITライセンス。自由に使用・配布可能です。
![螢幕擷取畫面 2026-02-17 004819](https://github.com/user-attachments/assets/6403bd0a-bf78-462a-b86b-4ab676d4e5aa)



If you want to create a standalone executable:
実行ファイルを作成するには、以下のコマンドを使用します：

```bash
pip install pyinstaller
pyinstaller --onefile --console merge.py
