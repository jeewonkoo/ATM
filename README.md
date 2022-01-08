# 
<div align=center>

  \
	![header](https://capsule-render.vercel.app/api?type=waving&&color=timeAuto&width=400&height=300&section=header&text=ATM%20Controller&fontSize=57&fontAlignY=35&desc=Simple+ATM+Implementation&descAlign=50&descAlignY=55&descSize=21&animation=twinkling)
</div>

## 

There are two files: **Bank.py** and **main.py**. **Bank.py** includes all the function implementation such as checkBalance, deposit, and withdraw. **Main.py** runs all the implemented function from **Bank.py**. \
\
Things to know about **Bank.py**: Since these two files are not implemented any REST API, RPC, network communication but functions/classes/methods, there are no database or information that can be compared to user input value. Therefore, for the insertCard function, the default value is **card**. If user enter any value other than **card**, the program cannot read user input value and will be automatically finished. Similiar for readPIN function, the default PIN number is **9999**, if user enter any value other than **9999**, the program prints message that **Invalid PIN number. Transaction failed.** and will be automatically finished. However, you can change default PIN value line 17 on **main.py** (below code block). As you can see, you can simply change number **9999** to any number you want.
<div align=center>

```
b1 = Bank(hash(9999), random.randint(1,10000))
```

</div>

## 
<div align=center>

  \
	![header](https://capsule-render.vercel.app/api?type=rounded&&color=timeAuto&width=400&height=200&section=header&text=%20INSTRUCTIONS&fontSize=60&fontAlignY=53&descAlignY=55&descSize=21&animation=twinkling)
</div>

# 
<div align=center>

Use below command to clone project

```
$ git clone https://github.com/jeewonkoo/ATM.git

```


Use below command to run project (Please make sure you are in same directory)

```
$ python3 main.py

```

</div>
