# sem4task1
Copy the countdown function below (refer to Section 5.8 in Downey "Think Python" for details) 

def countdown(n):

     if n <= 0:

          print('Blastoff!')

     else:

          print(n)

          countdown(n-1)

Write a new recursive function countup that expects a negative argument and counts “up” from that number. Output from running the function should look something like this:

>>> countup(-3)

-3

-2

-1

Blastoff!

Write a Python program that gets a number using keyboard input. (Remember to use input for Python 3 but raw_input for Python 2.)

If the number is positive, the program should call countdown. If the number is negative, the program should call countup. Choose for yourself which function to call (countdown or countup) for input of zero.

Upload the your python file to Github and make your repository public.
