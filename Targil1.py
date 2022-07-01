def my_func(x1,x2,x3):
    #checking type of var
    check_x1 = isinstance(x1,float)
    check_x2 = isinstance(x2, float)
    check_x3 = isinstance(x3, float)

    if (x1+x2+x3) == 0:
        return (print("Not a number – denominator equals zero"))
    if (check_x1 and check_x2 and check_x3):
        return float(((x1 + x2 + x3) * (x2 + x3) * x3) / (x1 + x2 + x3))
    else:
        print("Error: parameters should be float")
    return None


def convert(hours, minutes=0):

    if hours < 0 or minutes < 0:
        print("Input error!")
        exit(1)
    if isinstance(hours, float):
        h = str(hours)
        hours = float(h.split('.')[0])
        minutes = float(float(h.split('.')[1])/100*60)
          
    return (hours * 3600 + 60 * minutes)

