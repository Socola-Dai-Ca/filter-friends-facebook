import requests
import time
delay_time = 1
info = {}
tk = ''
die_count = 0
rank_count = 0

#check avaiable user
def delete_uid(uid):
	r = requests.get('https://graph.facebook.com/me/friends/'+uid+'?access_token='+tk+'&method=DELETE')
	if(r.status_code == 200):
		return True
	else:
		return False
def user_check(uid):
	r = requests.get('https://graph.facebook.com/'+uid+'?access_token='+tk+'&method=GET')
	if(r.status_code == 200):
		return False
	else:
		return True	
#check access token
def check_token(tk):
	r = requests.get('https://graph.facebook.com/me?access_token='+tk+'&method=GET')
	
	if(r.status_code == 200):
		inf = r.json()

		info['id_fb'] = inf['id']
		info['name']  = inf['name']
		return True
	else:
		return False
#get friends rank

def friend_rank():
	die_count = 0
	rank_count = 0
	query = '{"rank":"SELECT uid2, communication_rank FROM friend WHERE uid1 = me() ORDER BY communication_rank DESC LIMIT '+str(limit)+'","friends":"SELECT uid, name, sex, birthday_date, mutual_friend_count FROM user WHERE uid IN (SELECT uid2 FROM #rank) ORDER BY mutual_friend_count ASC LIMIT '+str(limit)+'"}'
	data_get = {
		'method' : 'GET', 
		'access_token' : tk,
		'q' : query
	};
	r = requests.get('https://graph.facebook.com/fql', params = data_get)
	data  = r.json()
	print('QUET THANH CONG DANG TIEN HANH XU LY')
	for res in data['data'][0]['fql_result_set']:
		time.sleep(delay_time)
		if (die.upper() == 'Y'):	
			
			if user_check(res['uid2']):
				if delete_uid(res['uid2']):
					die_count = die_count + 1
					print('deteled: '+res['uid2']+' (die, checkpoint)')
				else:
					print('delete error: '+res['uid2']+'')
		if (rank_delete.upper() == 'Y'):
			
			if(float(res['communication_rank']) == 0):
				rank_count = rank_count + 1
				if delete_uid(res['uid2']):
					print('deteled: '+res['uid2']+' (rank)')
				else:
					print('delete error: '+res['uid2']+'')
			
	print('Da xoa '+str(die_count)+' accs cp, die')
	print('Da xoa '+str(rank_count)+' accs khong tuong tac')


#input
tk = raw_input('>> Nhap access_token : ')
if tk == '' :
	print('access_token required !')
else:
	if check_token(tk):
		limit = input('Gioi han quet : ')
		rank_delete = raw_input('Xoa nguoi ko tuong tac(Y/N):  ')
		# avatar = raw_input('Xoa nguoi khong co avatar (Y/N): ')
		# die = raw_input('Xoa nick die, checkpoint: (Y/N): ')
		# mutual_friend = int(input('Ban be nho hon:  '))
		# gender = raw_input('Xoa nguoi co gioi tinh (0 = khong xoa, 1 = xoa nam, 2 = xoa nu, 3: xoa het): ')
		delay_time = int(input('>> Khoang cach moi lan xoa (s): '))

		friend_rank()
	else:
		print('access_token error')


