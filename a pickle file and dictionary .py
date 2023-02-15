try:
    f=open("ref_name.pkl","rb")

    ref_dictt=pickle.load(f)
    f.close()
except:
    ref_dictt={}
ref_dictt[ref_id]=name


f=open("ref_name.pkl","wb")
pickle.dump(ref_dictt,f)
f.close()

try:
    f=open("ref_embed.pkl","rb")

    embed_dictt=pickle.load(f)
    f.close()
except:
    embed_dictt={}
