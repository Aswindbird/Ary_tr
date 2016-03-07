print "1: 10->2\n2: 10->16\n3: 2->10\n4: 16->10\n5: 16->2\n6: 2->16\n"
c =int( raw_input("Input your choice:"))   #  c = choose

# 10->2
if c ==  1:
    print bin(int(raw_input("Input your number:")))
    

# 10->16
elif c == 2:
    print hex(int(raw_input("Input your number:")))
    

# 2->10
elif c ==3:
    print str(int(raw_input("Input your number:"),2))
    

# 16->10
elif c ==4:
    print str(int(raw_input("Input your number:"),16))
    

# 16->2
elif c == 5:
    s = str(int(raw_input("Input your number"),16))  #  s = step
    print bin(int(s))
    

# 2->16
elif c ==6:
    st = str(int(raw_input("Input your number:"),2))
    print hex(int(st))
    
