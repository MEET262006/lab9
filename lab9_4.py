lst=['madam','python',"malyalam",12321]
pali=list(filter(lambda s : str(s)==str(s)[::-1],lst))
print(pali)
