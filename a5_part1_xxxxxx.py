import string

#############################
# helper functions
#############################
def process_word(word):
    """
    Pre-processing for a word
    
    Parameters:
    word (str): Word that has to be pre-processed
    
    Returns:
    str : The preprocessed word 
    int : returns 0 if the word is not all alphabetic
    """
    punc_list = string.punctuation
    puncs = list(set(word).intersection(punc_list))
    if len(puncs) > 0:
        for punc in puncs:
            word = word.replace(punc,'')
    if word.isalpha(): # checks if all the characters are alphabetic
        return word.lower() # converting to lower case and returning
    else:
        return 0


def process_lines(lines):
    """
    Processing the contents of the document
    
    Parameters:
    lines (list): list of all the lines in the document
    
    Returns:
    dict : The dictionary of words and their corresponding lines
    
    """
    cnt = 0 #a variable to keep track of the line number
    dictionary = {}
    for line in lines:
        cnt += 1 
        words = line.split(' ')
        for word in words:
            if len(word) >= 2:
                new_word = process_word(word)
                if new_word != 0:
                    if new_word in dictionary: #checking if key already exists
                        if cnt not in dictionary[new_word]: # check to see if already key, value pair exists
                            dictionary[new_word].append(cnt)
                    else:
                        dictionary[new_word] = [cnt] # adding a new entry to the dictionary
    return dictionary
        
            
            
def intersection(lst1, lst2):
    """ Takes 2 strings and outputs a list of intersectinf characters between them """
    return list(set(lst1).intersection(lst2))
            
def display_output(out):
    """ A function for displaying the output of the query"""
    str_out = ''
    for val in out:
        str_out = str_out + str(val) + ' ' 
    print('The one or more words you entered co-existed in the following lines: '+ str_out )
                
                
        
#############################        
def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    while True:
        file_name = input("Enter the name of the file: ")
        try:
            f = open(file_name, 'r')
            return f
        except FileNotFoundError:
            print('There is no file with that name. Try again !')
      

    
def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    content = fp.read()
    fp.close()
    lines = content.split('\n')
    dict_words = process_lines(lines)
    return dict_words
        

        
    

def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
#    query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
    words = query.split(' ')
    cnt = 0 # checking for first word in the query
    out = []
    for word in words:
        
        new_word = process_word(word)
        if new_word == 'q':
            return False
        else:
            if new_word != 0: # check for all alphabetic word
                if new_word in D: # check if word exists in the file
                    if cnt == 0: 
                        out = D[new_word]
                        cnt += 1
                    out = intersection(out, D[new_word])
                else:
                    print('The word ' + new_word + ' not in the file !')
                    return True
            else:
                print('improper input !')
                return True
                    
    if len(out) == 0:
        print('The words ' + query + ' not in the file !')
        return True
    else:
        out.sort()
        display_output(out)
        return True



##############################
# main
##############################
file=open_file()
dd=read_file(file)



# YOUR CODE GOES HERE

while True:
    query=input("Enter one or more words separated by single spaces, or 'q' to quit: ").strip().lower()
    if find_coexistance(dd,query):
        pass
    else:
        break
    
    
    
    

