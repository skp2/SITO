import csv
M = 2 ** 26
def to_svml(file, train=True):
    with open(file,"r") as f:
        reader = csv.DictReader(f)
	for r in reader:
            del r['id']
	    r['hr'] = r['hour'][6:]
	    r['hour'] = r['hour'][4:6]
	    r['site_app_domain'] = r['site_domain']+r['app_domain']
	    r['site_app_catg'] = r['site_category']+r['app_category']
	    r['C1516'] = r['C15']+r['C16']
	    r['C151618'] = r['C15']+r['C16']+r['C18']
            r['C115'] = r['C1']+r['C15']
            r['C116'] = r['C1']+r['C16']
	    r['C118'] = r['C1']+r['C18']
	    r['C1151618'] = r['C1'] + r['C15']+r['C16']+r['C18']
	    y=-1
	    if train:
	        if int(r['click']) >0:
                    y=1
	        del r['click']
			
	    features = [ "{0}".format(abs(hash(v + '&' + k))% M) for k,v in r.items()]
	    yield "{0}".format(y) + ' | ' + ":1 ".join(features) + ':1'
		    

if __name__ == '__main__':
    with open('./data/train.vw','w') as vw:
        for i,t in enumerate(to_svml('./data/train.csv')):
            vw.write(t+'\n')
    with open('./data/test.vw','w') as vw:
        for i,t in enumerate(to_svml('./data/test.csv',train=False)):
            vw.write(t+'\n')
#  to_svml('./data/test.csv',train=False)
			