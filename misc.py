def center_window_on_monitor(self, w=400, h=200) -> None:
    ws = self.winfo_screenwidth()
    hs = self.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    g = [floor(i) for i in (w, h, x, y)]

    self.geometry('{0}x{1}+{2}+{3}'.format(*g))
