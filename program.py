import re

while True:
    print("---------------------------------------")
    print("Enter your sequence or press 0 for exit")
    seq = input("Sequence: ").upper()
    print("--------------------------------------------")
    valid_seq = "ATCGatcg"
    coding = ""
    check = all(n in valid_seq for n in seq)

    if seq == "0":
        break
    
    if check == False:
        print("--------------------------------------------")
        print("The sequence does NOT contain only the specified characters [A,T,C,G] \n")
    else:   
        start = [m.start() for m in re.finditer("ATG", seq)]
        TAG = [m.start() for m in re.finditer("TAG", seq)]
        TAA = [m.start() for m in re.finditer("TAA", seq)]
        TGA = [m.start() for m in re.finditer("TGA", seq)]
        stop = TAG + TAA + TGA
        stop.sort()

        
        for x in range(0, len(start)):
            for y in range(0, len(stop)):
                if stop[y] > start[x]:
                    if (stop[y]-start[x]) >3 and ((stop[y]-start[x]) % 3) == 0:
                        print(">", seq[start[x]:stop[y]+3])
                        coding = "yes"
                        break
        
        if coding == "yes":
            print(" ")
            print("The sequence includes the above coding regions \n")
        else:
            print("--------------------------------------------")
            print("The sequence does not include coding regions \n")




