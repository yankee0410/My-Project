import json
with open('class.json','r',encoding='utf-8') as f:
    datas=json.load(f)
print(datas,type(datas))
with open('newclass.json','w',encoding='utf-8') as f:
    dumpdata=json.dump(datas,f,ensure_ascii=False)
