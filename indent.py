x = 0
while x < 10:
    print(x)
    x = x + 1

def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    return f'{one} {delimiter} {two}'
    
a = get_summ("Learn", "python")
print(a.upper())
