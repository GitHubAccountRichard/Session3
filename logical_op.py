print(2 or 3)
print(2 and 3)
print(2 or 3 or 4 or 5)
print(2 and 3 and 0 and 5) # Cause 0 is a False value
print(0 or None or 7 or 0.0) # 7 is the only True one

#Generally the final output is what makes the chain true, basically the last number until the condition is satisfied

test = 10
test1 = 10
print(test is test1)

test2 = 10
test3= 12
print(test2 is not test3)
