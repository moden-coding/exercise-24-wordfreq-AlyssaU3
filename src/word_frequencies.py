#!/usr/bin/env python3

def word_frequencies(filename):
    with open(filename, "r") as a:
        word={}
        full_list=[]
        for line in a.readlines():
            lines= line.split()
            for words in lines:
                final=words.strip("""!\"#$%&'()*,-./:;?@[]_""")
                full_list.append(final)

        for word1 in full_list:
            if word1 in word:
                        word[word1]+=1
            else:
                        word[word1]=1
                #print(full_list)
        return word    
        
        
def main():
    d = word_frequencies("src/alice.txt")
    print (d["Carroll"])


    # if d["creating"] != 3:
    #    print("Incorrect count for word 'creating'!")
    # if d["Carroll"] != 3:
    #    print("Incorrect count for word 'Carroll'!")
    # if d["sleepy"] != 2:
    #    print("Incorrect count for word 'sleepy'!")
    # if d["Rabbit"] != 28:
    #    print("Incorrect count for word 'Rabbit'!")
    
    # if len(d) != 2424:
    #    print(f"Wrong number of words in the dictionary, should be 2424 but is {len(d)}")
    


if __name__ == "__main__":
    main()
