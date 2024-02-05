total_point = 0

question = input("UI stand for ")
if question.lower() == "user interface":
    total_point = total_point + 1
    print('Correct')
else:
    print('Incorrect')

print(f"Your total point is: {int(total_point/5*100)}%")



