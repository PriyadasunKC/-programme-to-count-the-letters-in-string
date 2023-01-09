name = input("Enter name : ")
count = 0

for letter in name:
    # we can check the spaces if found we can pass that iteration becore counting using "continue" keyword using belo code
    if(letter == " "):
        continue
    count += 1

    # we can check the spaces are available if find we can substract from the count using below code
    # count += 1
    # if(letter == " "):
    #     count -=1

print("{} character in your name".format(count))
