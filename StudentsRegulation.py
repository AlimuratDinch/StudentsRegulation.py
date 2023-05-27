MSG = '\nWelcome to the Teacher\'s Simple Class Calculator. Here\'s the list of options:\n  1- Enter student records (Name, ID, and 6 marks separated by commas)\n  2- Display the class average.\n  3- Display the information for a given student\n  4- List the entire class name and ID.\n  X- Exit \nSelect an option by entering its number or X to exit:'

N = input(MSG)
students = []      #creating an empty list of students
while N != 'X':
    
    if N == '1':

       
       x = input('\nEnter student record (separated fields by commas) or done:')
       dubid = []
       while x != "done" :          #finish the option 1 when it is typed 'done'

         
         y = x.split(',')           #spliting the x to many strings
         
         if len(y) == 8 and y[0].isalpha() and y[1].isdigit() == True and y[2].isdigit() and y[3].isdigit() and y[4].isdigit() and y[5].isdigit() and y[6].isdigit() and y[7].isdigit():  
             #making sure that no garde is missing and all grades are digit
             #name is entered without any quotes as for example in the assignement
             for i in y:
               
                 if len(i) == 3 and i.isdigit() == True:                          #getting rid of duble id
                     
                     dubid.append(i)
                     
                     if dubid.count(i) >= 2:                                      #if the list consist of identical IDs, signalize an error
                         print('Duplicate ID number.  Record rejected.')
                     
                     elif dubid.count(i) == 1:

                          students.append(y)                                      #Append a student list if everything is correct
                          
                          print('Record accepted')
                 

         elif len(y) != 8:                                                        #if the used did not entered full information, signalize an error
             print('Record incomplete.  Record rejected.')

         else:
             print('Record invalid.  Record rejected.')                           #if the information does not make sense, signalize an error

                  
         x = input('Enter student record (separated fields by commas) or done:')
         
               
   

    elif N == '2' and bool(students) == True:             #making sure that at least one students is entered
       
       z = []
       Sum = 0
       n_students = 0
 
       for i in students:

           n_students += 1                                 #count the number of students

           for val in i:
               if val.isdigit() == True and len(val) <=2:  # make sure that the values are all grades
                 
                   val = int(val)                          # converting strings to integers
                   z.append(val)                           #append all the graded to empty list 'z' for further summation
                  
                   Sum_0 = 0                
                   for Sum in z:                           #sum up all grades            
                      Sum_0 += Sum

       Average = round(Sum_0/n_students)                   #round the average to 
       print(Average)

       



    elif N == '3' and bool(students) == True:                    #making sure that at least one students is entered
        x = input('Enter the ID of the student:')
        error = []

        for i in students:
            z = []
            
            if i.count(x) == 1:                                  # make sure that ID is in the list, and work with the list of this ID

                for val in i:
                    
                    if val.isdigit() == True and len(val) <=2:   #convert the grades as stings to integers
                         val = int(val)
                         z.append(val)                           #append the grades
                        
                Sum_0 = 0        
                for Sum in z:
                   Sum_0 += Sum                                  #sum up all the grades

                def grade(r):
                    print('The information for',i[0],x,'total grade',Sum_0,'letter grade',r) # assign a grade as a letter with the information provided
                
                if Sum_0 >= 87: 
                    grade('A')
                    
                elif Sum_0 >= 75:
                    grade('B')
                    
                elif Sum_0 >=65:
                    grade('C')
                    
                else:
                    grade('F')

            elif i.count(x)== 0:   
                error.append(x)

        if len(error) == len(students) :        #print error if the lenght of other ids entered are equal to lenght of students
                                                #entered, therefore, the ID is not found
            print('\nerror')

                    


    elif N == '4' and bool(students) == True: #making sure that at least one students is entered
        
        for i in students:
            a = i[0]
            for val in i:
                if val.isalpha() == True:     #take the name
                    y = val.capitalize ()     #change it to capiltal letter

                    i.remove(a)               #remove the name with not capitalized name or with capitalized
                    i.insert(0,y)             #Insert a capitalized name at the begginig of the list
        students.sort()                       #sort the list by ascending order

        for i in students:
            print(i[0],i[1])                  #print the name with its assigned ID
        

        
                    
    N = input(MSG)
