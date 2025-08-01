import tkinter as tk
from tkinter import ttk
import webbrowser

class VIPVideoApp:
    def __init__(self, root):
        self.root = root
        self.root.title('VIP追剧神器 - 高级版')
        self.root.geometry('550x300')
        self.root.configure(bg="#1e1e2f")
        self.root.resizable(False, False)

        self.style = ttk.Style()
        self.customize_style()
        self.create_widgets()

    def customize_style(self):
        # 使用默认主题基础
        self.style.theme_use('clam')

        # 字体和颜色定制
        self.style.configure("TLabel",
                             foreground="white",
                             background="#1e1e2f",
                             font=("Segoe UI", 11))

        self.style.configure("TEntry",
                             foreground="black",
                             fieldbackground="#ffffff",
                             font=("Segoe UI", 11))

        self.style.configure("TButton",
                             font=("Segoe UI", 10, "bold"),
                             foreground="white",
                             background="#4e73df",
                             padding=6)

        self.style.map("TButton",
                       background=[('active', '#2e59d9'), ('pressed', '#1c396a')])

    def create_widgets(self):
        # 标题
        title_label = ttk.Label(self.root, text="VIP 视频解析工具", font=("Segoe UI", 18, "bold"))
        title_label.grid(row=0, column=0, columnspan=4, pady=(15, 10))

        # 输入区域
        ttk.Label(self.root, text='视频网址：').grid(row=1, column=0, padx=15, pady=10, sticky="e")
        self.entry_movie_link = ttk.Entry(self.root, width=40)
        self.entry_movie_link.grid(row=1, column=1, columnspan=2, padx=5, pady=10)

        clear_button = ttk.Button(self.root, text='清空', command=self.empty)
        clear_button.grid(row=1, column=3, padx=10)

        # 视频平台按钮
        ttk.Button(self.root, text='爱奇艺', command=self.open_iqy).grid(row=2, column=0, padx=15, pady=10)
        ttk.Button(self.root, text='腾讯视频', command=self.open_tx).grid(row=2, column=1, padx=15, pady=10)
        ttk.Button(self.root, text='优酷视频', command=self.open_yq).grid(row=2, column=2, padx=15, pady=10)

        play_button = ttk.Button(self.root, text='播放VIP视频', command=self.play_video)
        play_button.grid(row=2, column=3, padx=10, pady=10)

        # 提示
        tip_label = tk.Label(self.root,
                             text="⚠️ 本软件仅限学习使用，严禁用于非法用途。",
                             fg="#ff5555",
                             bg="#1e1e2f",
                             font=("Segoe UI", 10, "italic"))
        tip_label.grid(row=3, column=0, columnspan=4, pady=30)

    def open_iqy(self):
        webbrowser.open('https://www.iqiyi.com')

    def open_tx(self):
        webbrowser.open('https://v.qq.com')

    def open_yq(self):
        webbrowser.open('https://www.youku.com/')

    def play_video(self):
        video = self.entry_movie_link.get().strip()
        if video:
            webbrowser.open('https://jx.xmflv.cc/?url=' + video)

    def empty(self):
        self.entry_movie_link.delete(0, tk.END)

if __name__ == '__main__':
    root = tk.Tk()
    app = VIPVideoApp(root)
    root.mainloop()
