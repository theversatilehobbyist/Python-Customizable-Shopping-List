# The Shopping List
list = ['example food', 'example food', 'example food']

#Commands
print('Welcome to Your Personalized Shopping List!')
print('')
print(' To add an item to the list please just type the word \'add\'')
print('')
print(' To check the if a certain item is in the list please just type the word \'check\'')
print('')
print(' And to view the entire list please type the word \'view\'')
print('')

#Input
b = input('Enter the command you would like to give the Shopping List ')
val = b
#View Entire List
if val == 'view' or 'View':
    print('List Items')
    for x in list:
        print(x)

#Or Else
else:
    print('Sorry we didn\'t recognize that command')
