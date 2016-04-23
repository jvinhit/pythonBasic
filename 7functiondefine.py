def tinhtong():
    print('day la ham tinh tong')

tinhtong()

def bitcointousd(btc):
    amount = btc * 27
    print(btc ,' btc ', ' = ' , amount, ' usd')


bitcointousd(10)


def allow_dating(my_ages):
    age = my_ages*10 + 7
    return  age

print(allow_dating(10))



'''defaul value argument'''
def get_gender(sex="deobiet"):
    if sex is "biet":
        print('gioi tinh cua tao la ', sex)
    elif sex is "trai":
        print('tao la con trai')
    else:
        print(sex)


get_gender()
get_gender("bd")
get_gender("biet")


'''variable scope cung nhu nhung ngon ngu lap trinh khac, neu khai bao global thi truy cap moi noi, con khai bao local thi truy dc truy cap trong tam vuc bien khai bao'''
