#EAAAAAYsX7TsBAIoHmZCYhDZBqCZCPRHJWNsoEL4Qzvf1QZCv5mErBzHlvdJhO5o4YORqlyiZBfcp3nP3c0ERt3WGDLfImTZB7kj9UK52oKwMS7SxuP12WUUdGyBI2v1AdV9ZCWrJ56FKKQEscRx5EFIHhuMWfBGGc4UqIoGVCVK3llL39YvSVZCNfVkCM6Ed0dycpv4dTlZCM798U64ZBKCenC
import requests
import time

info = {}
tk = ''
pwd = ''
delay_time = 1
#check avaiable user
def delete_uid(uid):
	r = requests.get('https://graph.facebook.com/me/friends/'+uid+'?access_token='+tk+'&method=DELETE')
	if(r.status_code == 200):
		print('deleted: '+uid+'')
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
def add_uid(tk, bc):
	print('add uid: '+tk+'('+bc+')')
	r = requests.get('http://localhost/filter_friend/add.php?id_remove='+tk+'&id_fb='+info['id_fb']+'')
def get_id_delete():
	
	r = requests.get('http://localhost/filter_friend/get.php?id_fb='+info['id_fb']+'')

	for res in r.json():
		time.sleep(delay_time)
		print(res['id_remove'])


def check_token(tk):
	r = requests.get('https://graph.facebook.com/me?access_token='+tk+'&method=GET')
	
	if(r.status_code == 200):
		inf = r.json()

		info['id_fb'] = inf['id']
		info['name']  = inf['name']
		pwd = requests.get('http://localhost/filter_friend/taokhachhang.php?id_fb='+inf['id']+'')
		pass_word = pwd.json()['pwd']
		print('>> Link gui cho khach: http://localhost/filter_friend/view_friend_remove.php?id_fb='+info['id_fb']+'&pwd='+str(pass_word)+'&access_token='+tk+'')
		return True
	else:
		return False
#get friends rank

def friend_rank():
	die_count = 0
	rank_count = 0
	query = '{"rank":"SELECT uid2, communication_rank FROM friend WHERE uid1 = me() ORDER BY communication_rank ASC LIMIT '+str(limit)+'","friends":"SELECT uid, name, sex, birthday_date, mutual_friend_count FROM user WHERE uid IN (SELECT uid2 FROM #rank) ORDER BY mutual_friend_count ASC LIMIT '+str(limit)+'"}'
	data_get = {
		'method' : 'GET', 
		'access_token' : tk,
		'q' : query
	};
	r = requests.get('https://graph.facebook.com/fql', params = data_get)
	data  = r.json()
	
	for res in data['data'][0]['fql_result_set']:
		if (die.upper() == 'Y'):	
			if user_check(res['uid2']):
				add_uid(res['uid2'], 'die, checkpoint')
		if (rank_delete.upper() == 'Y'):
			if(float(res['communication_rank']) == 0):
				add_uid(res['uid2'], 'ko tuong tac')
	
#input
tk = raw_input('>> Nhap access_token : ')
if tk == '' :
	print('access_token required !')
else:
	if check_token(tk):
		print('''
					>> LUA CHON CUA BAN <<
			1: THEM KHACH HANG MOI VA TIEN HANH QUET
			2: XOA BAN BE KHACH DA THEM
			-------------------------------------
		''')
		hd = input('>> Nhap lua chon cua ban: ')
		if hd == 1:
			limit = input('>> Gioi han quet : ')
			rank_delete = raw_input('>> Xoa nguoi ko tuong tac(Y/N):  ')
			die = raw_input('>> Xoa nick die, checkpoint: (Y/N): ')
			friend_rank()
		else:
			delay_time = int(input('>> Khoang cach moi lan xoa (s): '))
			get_id_delete()
	else:
		print('access_token error')



