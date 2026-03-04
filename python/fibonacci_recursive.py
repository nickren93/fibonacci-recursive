
#   0, 1, 1, 2, 3, 5, 8

def fibonacci(n):

    # a,b = 0, 1

    # for n in range(1, n+1):
    #     a,b = b, a+b

    # return a

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)




    