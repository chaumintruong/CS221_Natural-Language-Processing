from os import write

def combineText(from_, to_): # từ 2 array[str] mình gộp lại thành 1 array[str] chứa tiếng Anh và Tiếng Việt
    text = []
    for i in range(len(from_)):
        text.append(from_[i][:-1] + "\t" + to_[i])
    text[-1] = text[-1][:-1] # do có ký tự xuống dòng nên dòng code này chỉ để làm mất kí tự xuống dòng của câu cuối cùng trong file
    return text
        
def write_Text_into_file(text, my_file): # ghi vào file vừa tạo
    for i in text_:
        my_file.write(i)
    
    return my_file

Viee = open("com_vie_3.txt", "r", encoding= 'utf-8') # truy xuất file tại thư mục chứa code này
En = open("com_en_3.txt", "r", encoding= 'utf-8') # truy xuất file tại thư mục chứa code này
strViee = Viee.readlines() # hàm readlines sẽ đọc từng dòng trong file text và lưu vào 1 cái mảng với từng phần tử trong mảng là 1 string (là 1 câu trong file text)
strEn = En.readlines() # hàm readlines sẽ đọc từng dòng trong file text và lưu vào 1 cái mảng với từng phần tử trong mảng là 1 string (là 1 câu trong file text)
text_ = combineText(strEn, strViee) # gọi hàm ở trên để kết hợp 2 file lại
my_file = open("en_vie_11.txt","w+",encoding= 'utf-8') # tạo file mới
my_file = write_Text_into_file(text_, my_file) # gọi hàm để ghi dữ liệu vào file mới tạo






""" This code below just modify 1 text file downloaded from manythings.org/anki 
for i in text:
    cnt = 0
    for j in range(len(i)): 
        if i[j] == '.' or i[j] == '?' or i[j] == '!':
            cnt += 1
        if cnt == 2:
            if len(i[0:j+1].split("\t")) > 1:
                if i[j] != ".":
                    x = i[0:j] + "\t" + i[j]
                else: x = i[0:j+1]
                text_.append(x+"\n")
            #print(i)
            break
#print(text_)
my_file = open("eng-vie.txt","w",encoding= 'utf-8')

"""