def hello(): 
    print("Hello user")

def pack(item1, item2, item3):
    return ([item1, item2, item3])

def eat_lunch(lunch_list):
    if len(lunch_list) == 0:
        print("My lunchbox is empty")
    else:
        for i in range(len(lunch_list)):
            # print(i)
            if i == 0:
                print("First I have", lunch_list[i])
            else:
                print("Then I have", lunch_list[i])


hello()

print(pack('clothes', 'phone', 'charger'))

eat_lunch([])
eat_lunch(['spaghetti'])
eat_lunch(['sandwich', 'drink'])
eat_lunch(['chicken', 'drink', 'carrots'])