import tkinter as tk
import tkinter.filedialog
# import typing as t
from pathlib import Path
# import os
import tkinter.messagebox as tkmb
import time


class MainWindow(tk.Tk):

    def __init__(self) -> None:
        super().__init__()

        self.geometry('500x200')
        self.resizable(False, False)
        self.title('Simple Image Converter')

        self.selected_image_types = {'input': False, 'output': False}
        self.image_types = {
            'input': ['jpg', 'png', 'webp', 'all'],
            'output': ['jpg', 'png', 'webp']}

        rb1 = tk.Radiobutton(
            self, text='Folder',
            command=lambda: self.change_convert_ready_status('Folder', 0))
        rb2 = tk.Radiobutton(
            self, text='File(s)',
            command=lambda: self.change_convert_ready_status('File(s)', 1))
        rb1.grid(row=1, column=0)
        rb2.grid(row=1, column=1)

        self.l1 = tk.Label(self, text='No type selected', fg='red')
        self.l1.grid(row=1, column=2)

        tk.Label(self, text='Input file/folder:').grid(row=2, column=0)
        tk.Label(self, text='Output folder:').grid(row=3, column=0)

        self.b1 = tk.Button(self, text='Select path',
                            command=lambda: self.get_path('input'),
                            state='disabled')
        self.b2 = tk.Button(self, text='Select path',
                            command=lambda: self.get_path('output'),
                            state='disabled')
        self.b1.grid(row=2, column=1)
        self.b2.grid(row=3, column=1)

        # TODO: Fix this damn bug where only the last item is selected..
        for i, (k, v) in enumerate(self.image_types.items()):
            for item in v:
                rb = tk.Radiobutton(
                    self, text=item,
                    command=lambda: self.image_conversion_type(k, item))
                rb.grid(row=i + 2, column=self.image_types[k].index(item) + 2)

        self.convert_button = tk.Button(
            self, text='Convert', command=self.file_conversion,
            state='disabled')
        self.convert_button.grid(row=5, column=1)

        self.l2 = tk.Label(self, text='No paths selected', fg='red')
        self.l2.grid(row=5, column=2)

        tk.Button(
            self, text='Advanced settings',
            command=lambda: AdvancedWindow(self),
            state='disabled'
        ).grid(row=4, column=1)

    def get_path(self, directed_to: str) -> None:
        if directed_to == 'input':
            if self.file_s:
                p = tkinter.filedialog.askopenfilenames(initialdir=Path.cwd())

            else:
                p = tkinter.filedialog.askdirectory(initialdir=Path.cwd())

        else:
            p = tkinter.filedialog.askdirectory(initialdir=Path.cwd())

        self.paths[directed_to] = p

        if all(v for v in self.paths.values()):
            self.convert_button['state'] = 'normal'

    def image_conversion_type(self, in_out: str, image_type: str) -> None:
        self.selected_image_types[in_out] = image_type
        print(in_out, image_type, self.selected_image_types)

    def change_convert_ready_status(self, _type: str, var: int) -> None:
        self.paths = {'input': False, 'output': False}
        self.l1['fg'] = 'green'
        self.l1['text'] = f'Selecting for {_type}.'
        self.file_s = var
        self.b1['state'], self.b2['state'] = 'normal', 'normal'
        self.convert_button['state'] = 'disabled'

    def file_conversion(self) -> None:
        print(self.paths)
        return
        answer = tkmb.askokcancel(
            'Conversion Confirmation',
            'Are you sure you want these image(s) to be converted?')

        if answer:
            pass


class AdvancedWindow(tk.Toplevel):

    def __init__(self, master, *args, **kwargs) -> None:
        super().__init__(master)

        self.master = master
        self.grab_set()
        self.focus_set()
        self.transient(master)

        self.geometry('400x75')
        self.title('Advanced Settings')

        self.thread_amount = tk.IntVar()
        self.recursive_amount = tk.IntVar()

        self.l1 = tk.Label(self, text='Thread amount:')
        self.l1.grid()

        e1 = tk.Entry(self, textvariable=self.thread_amount)
        e1.grid(row=0, column=1)
        e1.bind('<Return>', self.set_thread_amount)

        tk.Radiobutton(
            self, text='Convert resursively into folders',
            command=self.activate_resursiveness
        ).grid(row=1)

        self.e2 = tk.Entry(
            self, textvariable=self.recursive_amount, state='disabled')
        self.e2.grid(row=3, column=1)
        self.e2.bind('<Return>', self.set_recursive_amount)

    def set_thread_amount(self, event) -> None:
        self.master.thread_amount = self.thread_amount.get()

    def activate_resursiveness(self) -> None:
        self.e2['state'] = 'normal'

    def set_recursive_amount(self, event) -> None:
        self.master.recursive_amount = self.recursive_folders.get()


if __name__ == "__main__":
    MainWindow().mainloop()
