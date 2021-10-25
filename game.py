import numpy as np

number = np.random.randint(1,101)

count = 0

while True:
    count+=1
    predict_number = int(input('Choose youre number from 1 to 100:'))
    
    if predict_number>number:
        print('Number must be lower!')
        
    elif predict_number<number:
        print('Number must be upper!')
        
    else:
        print(f"You're right! This number = {number}, for {count} tries.")
        break