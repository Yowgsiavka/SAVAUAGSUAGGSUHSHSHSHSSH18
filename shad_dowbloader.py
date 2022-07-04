from rubpy.shad import Bot
from threading import Thread
from requests import get
from random import randint

# defines...
def downloadWithLink(bot,chat,text,my_guid,):
	try:
		text=text[5:-1]
		file_byte=get(text).content
		rsf = bot.requestSendFile(f'file{randint(1000,10000)}.zip', len(file_byte), 'mp4')
		if rsf!='many_request':
			access = bot.fileUpload(file_byte, rsf['access_hash_send'], rsf['id'], rsf['upload_url'])
			bot.sendFile(my_guid,rsf['id'] , 'mp4', rsf['dc_id'] , access, 'file{randint(10000,100000000)}.mp4', len(file_byte))
	except:
		try:
			bot.sendMessage(my_guid, 'خطا مجددا تلاش کنید')
		except:pass

bot=Bot('nafhqlyiuzzwhuibakkxmleorcsyvgxm')
answered=[درحال دانلود]
my_guid="u0jdT069f558380a2a73bd907c8e74ed"

while 1:
	try:
		chats:list=bot.getChatsUpdate()
		if chats!=[]:
			for chat in chats:
				if chat['abs_object']['type']=='User':
					 text:str=bot.getMessagesInfo(chat['object_guid'], [chat['last_message']['message_id']])[0]['text']
					 if 'SendMessages' in chat['access'] and chat['last_message']['type'] == 'Text':
					 	if not chat['object_guid']+chat['last_message']['message_id'] in answered:
					 		if chat['last_message']["author_object_guid"]==str(my_guid):
					 			if text.startswith('!dl ['):
					 				Thread(target=downloadWithLink,args=(bot,chat,text,my_guid,)).start()

					 			answered.append(chat['object_guid']+chat['last_message']['message_id'])
	except:pass