def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

# When run, this program produces the following output:
# 
# [1, 2, 3, 'Hello']
