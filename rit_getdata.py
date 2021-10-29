import os
from datetime import date
import pickle


FOLDER = f"/Users/rfcb/Documents/Scripts/RIT_covid_tracker/data"
HTML = f"{FOLDER}/rit-dashboard.html"
PICKLE = f"{FOLDER}/data.pickle"
WEBPAGE = "https://www.rit.edu/ready/fall-2021-dashboard"

PRINT = 0



def tprint(arg):
    if PRINT:
        print(arg)

def main():
    os.system(f"curl -s -o {HTML} {WEBPAGE}")

    dict = {}
    numbers = list()
    
    with open(PICKLE, "rb") as f:
        dict = pickle.load(f)
    
    try:
        os.system(f"rm {PICKLE}")
    except:
        pass
    

    with open(HTML) as f:

        i=0
        ret = False
        
        for line in f:
            if ret:
                numbers.append(line.strip())
                ret=False
            elif """<p class="card-header position-relative pb-0  font-weight-normal">""" in line:
                ret = True
        tprint(f"{numbers[0]} new student cases in last 14 days\n{numbers[1]} new staff cases in the last 14 days\n{numbers[2]} total student cases this semester\n{numbers[3]} staff cases this semester\n")

    dict[f"{date.today()}"] = numbers
    tprint(dict)

    with open(PICKLE, "xb") as f:
        pickle.dump(dict, f)


if __name__ == "__main__":
    main()