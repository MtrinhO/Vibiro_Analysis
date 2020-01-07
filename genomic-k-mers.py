#Identifies the amount of times a k-mer appears in "Text"
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

#Counter function- iteratively adds frequency of k-mer
def FrequencyMap(Text,k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
    #Iteratively adds count of k-mer to freq
    for i in range(n-k+1):
        for Pattern in freq:
            if Pattern == Text[i:i+k]:
                freq[Pattern]=freq[Pattern]+1
    return freq

#Return the highest frequency k-mer (highest value LIST. terms) in highest_freq
def FrequentWords(Text,k):
    freq=FrequencyMap(Text,k)
    highest_freq=[]
    maximum = max(freq.values())
    #Searches for highest frequency k-mer in freq, appends it/them to the list
    for Pattern in freq:
        if maximum == freq[Pattern]:
            highest_freq.append(Pattern)
    return highest_freq

#Return the highest frequency k-mer (highest value DIC. terms) in highest_freq
    def FrequentWordsDic(Text,k):
        freq=FrequencyMap(Text,k)
        highest_freq_dic={}
        maximum = max(freq.values())
        #Searches for highest frequency k-mer in freq, appends it/them to the list
        for Pattern in freq:
            if maximum == freq[Pattern]:
                highest_freq_dic.update({Pattern:freq[Pattern]})
        return highest_freq_dic

    #Return the starting locations of specified k-mer in a genome
def PatternMatching(Text, Pattern):
    positions = [] # output variable
    n = len(Text)
    p = len(Pattern)
    for i in range(n-p+1):
        if Pattern == Text[i:i+p]:
            positions.append(i)
    return positions
