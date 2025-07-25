

def numberToWords(num):
    if num==0:
        return "Zero"
    
    below_20=[
        "", "One", "Two", "Three", "Four", "Five", "Six",
        "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
        "Thirteen", "Fourteen", "Fifteen", "Sixteen",
        "Seventeen", "Eighteen", "Nineteen"
    ]
    tens=[
        "", "", "Twenty", "Thirty", "Forty",
        "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
    ]
    scales=["","Thousand", "Million", "Billion"]

    def three_digit_to_words(n):
        if n==0:
            return []
        if n<20:
            return [below_20[n]]
        if n<100:
            return [tens[n//10]] + three_digit_to_words(n%10)
        return [below_20[n//100],"Hundred"]+three_digit_to_words(n%100)
    
    words:list[str]=[]
    scale_idx=0

    while num>0:
        chunk=num%1000
        if chunk:
            words=three_digit_to_words(chunk)+(
                [scales[scale_idx]] if scales[scale_idx] else []
            ) + words
        num //=1000
        scale_idx +=1
    
    return " ".join(words)

if __name__=="__main__":
    test_values=[123,12345,1234567,0]
    for val in test_values:
        print(f"{val}->{numberToWords(val)}")