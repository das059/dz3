from compare import compare
pairs=[
    ('Рука','Нога'),
    ('Свет','Тьма'),
    ('Полка','Палка'),
    ('Cat','Dog'),

]
if __name__=="__main__":
    for s,t in pairs:
        print(s,t, compare(s,t))
