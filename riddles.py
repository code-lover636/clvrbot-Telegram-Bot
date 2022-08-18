import csv, random

def organize():
    with open("riddle.txt","r+") as f:
        content = f.readlines()
        count = 43
        for line in content:
            if line[0]==" ":
                content[content.index(line)]=line[1:]
            content[content.index(line)] = (count,line[:line.index("(Answer")],line[line.index("(Answer"):-1])
            count += 1
        with open("riddle.csv","a",newline="") as f1:
            writer = csv.writer(f1)
            writer.writerows(content)

def random_riddle():
    with open("riddle.csv","r") as f:
        r = list(csv.reader(f))
        qns = random.choice(r)
        print(qns[1])
        qns[2] = qns[2].replace("(", "").replace(")", "")
        print(qns[2])
        return qns

if __name__ == "__main__":
    random_riddle()
        
        