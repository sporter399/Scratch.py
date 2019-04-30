from random import randint

 
def function(my_list):
    
   for num in range(len(my_list)-1, 0, -1):
       print(num)

def main():

    
    my_list = [87, 11, 22, 34599, 2, 9, 58]
    function(my_list)

if __name__ == "__main__":
    main()

