from tkinter import *


def start_main_page():
    def start_game(args):
        main_window.destroy()
        if args == 1:
            from packages import APPS
            APPS.main()
        elif args == 2:
            from packages import PROGRAMS
            PROGRAMS.main()
        elif args == 3:
            from packages import PC
            PC.main()
        elif args == 4:
            from packages import GAMES1
            GAMES1.main()
        elif args == 5:
            from packages import OS
            OS.main()
        elif args == 6:
            from packages import ANTIVIRUS
            ANTIVIRUS.main()

    def option():

        lab_img1 = Button(
            main_window,
            text="Select",
            bg='#0066ff',
            border=0,
            justify='center',
            font=("Arial", 12)

        )
        sel_btn1 = Button(
            text="APPS",
            width=20,
            borderwidth=8,
            font=("", 18),
            fg="#ff3333",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(1),
        )

        sel_btn2 = Button(
            text="PROGRAMS",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(2),
        )

        sel_btn3 = Button(
            text="PC",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(3),
        )

        sel_btn4 = Button(
            text="GAMES1",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(4),
        )

        sel_btn5 = Button(
            text="OS",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(5),
        )

        sel_btn6 = Button(
            text="ANTIVIRUS",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#99ffd6",
            cursor="hand2",
            command=lambda: start_game(6),
        )

        lab_img1.grid(row=0, column=0, padx=20)
        sel_btn1.grid(row=0, column=4, pady=(10, 0), padx=50, )
        sel_btn2.grid(row=1, column=4, pady=(10, 0), padx=50, )
        sel_btn3.grid(row=2, column=4, pady=(10, 0), padx=50, )
        sel_btn4.grid(row=3, column=4, pady=(10, 0), padx=50, )
        sel_btn5.grid(row=4, column=4, pady=(10, 0), padx=50, )
        sel_btn6.grid(row=5, column=4, pady=(10, 0), padx=50, )

    def show_option():
        start_btn.destroy()

        lab_img.destroy()
        option()

    main_window = Tk()

    main_window.geometry("500x500+500+150")
    main_window.resizable(0, 0)
    main_window.title("Guess the Word")
    main_window.configure(background="#0066ff")
    

    img1 = PhotoImage(file="back.png")

    lab_img = Label(
        main_window,
        text="Guess the Word Game",
        bg='#0066ff',
        font=("Courier", 28)
    )
    lab_img.pack(pady=(50, 0))

    start_btn = Button(
        main_window,
        text="Start",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#99ffd6",
        font=("", 13),
        cursor="hand2",
        command=show_option,
    )
    start_btn.pack(pady=(50, 20))

    main_window.mainloop()


start_main_page()
