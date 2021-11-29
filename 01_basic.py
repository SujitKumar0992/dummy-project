# EXCEPTION HANDLING:
#-------------------------------

# Everey Exception in python is a class....
#         All exception classes are child classes of BasicException...


#______________________________________________________
# Customize exception Handling by using (try-except):
#-------------------------------------------------------


#___________________________
# Without try except:
#---------------------------

'''print('hello')
print(10/0)  # ZeroDivisionError
print("hi")'''

#note: abnormal termination/non graceful termination

#________________________
#with try-except:
#-------------------------

print('hello')

try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)

print("hi")

#note: Normal termination / graceful termination..



# how to print exception information:
#-----------------------------------------

try:
    print(10/0)
except ZeroDivisionError as msg:
    print("exception raised and its description is :",msg)