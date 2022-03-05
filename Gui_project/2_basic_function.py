import tkinter.ttk as ttk
from tkinter import * # __all__
from tkinter import filedialog
import tkinter.messagebox as msgbox

root = Tk()
root.title('SB GUI')

# 파일 함수
def add_file():
    files = filedialog.askopenfilenames(title='이미지 파일을 선택하세요.', filetypes=(('PNG 파일', '*.png'),('jpg 파일','*.jpg'),('그 외 파일','*.*')), initialdir = r'/User')

    # 선택한 파일 목록
    for file in files:
        list_file.insert(END, file)

def del_file():
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# 저장 경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected is None:
        return
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# 시작
def start():
    # 각 옵션 값 확인
    
    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning('경고',' 선택된 파일이 없습니다.')
        return

    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning('경고', '저장 경로가 없습니다.')

# 파일 프레인 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill='x', padx=5, pady=5)

btn_add_file = Button(file_frame, padx= 5, pady=5, width=12, text='파일추가', command=add_file)
btn_add_file.pack(side='left')

btn_del_file = Button(file_frame, padx= 5, pady=5, width=12, text='선택삭제', command=del_file)
btn_del_file.pack(side='right')

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill= 'both', padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side='right', fill='y')

list_file = Listbox(list_frame, selectmode='extended', height=15, yscrollcommand=scrollbar.set)
list_file.pack(side='left', fill='both', expand=True)
scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text='저장경로')
path_frame.pack(fill='x', padx=5, pady=5, ipady = 5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side='left', fill='x', expand=True, padx=5, pady=5)

btn_dest_path = Button(path_frame, text='찾아보기', width=10, command=browse_dest_path)
btn_dest_path.pack(side='right', padx=5, pady=5)

# 옵션 프레임
option_frame = LabelFrame(root, text='옵션')
option_frame.pack(padx=5, pady=5, ipady = 5)

# 1. 가로 넓이 옵션
# 가로 넓이 레이블
lbl_width = Label(option_frame, text='가로넓이', width=8)
lbl_width.pack(side='left', padx=5, pady=5)

# 가로 넓이 콤보
opt_witdth = ['원본유지','1024', '800', '640']
cmb_width = ttk.Combobox(option_frame, state='readonly', values=opt_witdth, width=8)
cmb_width.current(0)
cmb_width.pack(side='left', padx=5, pady=5)

# 2. 간격 옵션
# 간격 레이블
lbl_space = Label(option_frame, text='간격', width=8)
lbl_space.pack(side='left', padx=5, pady=5)

# 간격 콤보
opt_space = ['없음','좁게', '보통', '넓게']
cmb_space = ttk.Combobox(option_frame, state='readonly', values=opt_space, width=8)
cmb_space.current(0)
cmb_space.pack(side='left', padx=5, pady=5)

# 파일 포맷 옵션
# 파일 포맷 레이블
lbl_format = Label(option_frame, text='포맷', width=8)
lbl_format.pack(side='left', padx=5, pady=5)

# 파일 포맷 콤보
opt_format = ['PNG','JPG', 'SVG']
cmb_format = ttk.Combobox(option_frame, state='readonly', values=opt_format, width=8)
cmb_format.current(0)
cmb_format.pack(side='left', padx=5, pady=5)

# 진행 상황 Progress Bar
progress_frame = LabelFrame(root, text='진행상황')
progress_frame.pack(fill='x', padx=5, pady=5, ipady = 5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(progress_frame, maximum=100, variable=p_var)
progress_bar.pack(fill='both', padx=5, pady=5)

# 실행 프레임
run_frame = Frame(root)
run_frame.pack(fill='x', padx=5, pady=5)

btn_close = Button(run_frame, padx=5, pady=5, text='닫기', width= 12, command=root.quit)
btn_close.pack(side='right', padx=5, pady=5)

btn_start = Button(run_frame, padx=5, pady=5, text='시작', width= 12, command=start)
btn_start.pack(side='right', padx=5, pady=5)

root.resizable(False, False)
root.mainloop()