class script(object):
    START_TXT = """<b>π Hello {},

I Can Provide Movies And Series, Just Add Me In Your Group And Make Me Admin!!

π Powered by: @Movies7x</b>
"""
    HELP_TXT = """<b>π§πΎπππ π¬π. {} π¨π'π π¬π π§πΎππ π¬ππ½πππΎ</b>"""

    ABOUT_TXT = """<b>β― MΚ Nα΄α΄α΄ : {}</b>

<b>β― CΚα΄Ι΄Ι΄α΄Κ : @Movies7x</b>

<b>β― Bα΄ΙͺΚα΄ Sα΄α΄α΄α΄s : α΄ 5.0.1 [Sα΄α΄ΚΚα΄]</b>"""
    
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Movies7x)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features 

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specified user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - <code>to get the rescent errors</code>
β’ /stats - <code>to get status of files in db.</code>
β’ /delete - <code>to delete a specific file from db.</code>
β’ /users - <code>to get list of my users and ids.</code>
β’ /chats - <code>to get list of the my chats and ids </code>
β’ /leave  - <code>to leave from a chat.</code>
β’ /disable  -  <code>do disable a chat.</code>
β’ /ban  - <code>to ban a user.</code>
β’ /unban  - <code>to unban a user.</code>
β’ /channel - <code>to get list of total connected channels</code>
β’ /broadcast - <code>to broadcast a message to all users</code>
β’ /grp_broadcast - <code>to broadcast a message to all connected groups</code>
β’ /dellfiles - <code>to delete specific name files form the database</code>"""

    STATUS_TXT = """π³πππΊπ π₯πππΎπ: <code>{}</code>
π³πππΊπ π¬πΎππ»πΎππ: <code>{}</code>
π³πππΊπ π’ππΊππ: <code>{}</code>
π΄ππΎπ½ π²ππππΊππΎ: <code>{}</code>
 """
    PRIVATEBOT_TXT = """<b>Κα΄ΚΚα΄ {}, Ι΄Ιͺα΄α΄ α΄α΄ α΄α΄α΄α΄ Κα΄α΄.

Ιͺ'α΄ α΄α΄sα΄ α΄ sΙͺα΄α΄Κα΄ α΄Κα΄-?α΄Ι΄α΄α΄Ιͺα΄Ι΄α΄α΄ α΄α΄α΄α΄?ΙͺΚα΄α΄Κ Κα΄α΄.

Ιͺα΄'s α΄α΄sΚ α΄α΄ α΄sα΄ α΄α΄, α΄α΄sα΄ α΄α΄α΄ α΄α΄ α΄α΄ Κα΄α΄Κ Ι’Κα΄α΄α΄ α΄s α΄α΄α΄ΙͺΙ΄.</b>"""

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""

    IMDB_TEMPLATE_TXT = """<i><b>π Movie Name</b></i> : <i><b><a href={url}>{title}</a></b></i>
<i><b>ποΈ Release Date</b></i> : <i><b>{release_date}</b></i>

<i><b>β­ IMDB Rating</b></i> : <i><b><a href={url}/ratings>{rating}/10</a></b></i>
<i><b>ποΈ Genres</b></i> : <i><b>{genres}</b></i>

<i><b>π©π»βπ» Requested By</b></i> : <i><b>{message.from_user.mention}</b></i>
<i><b>π Group</b></i> : <i><b>{message.chat.title}</b></i>"""

    VERIFED_TXT = """<b>Κα΄ΚΚα΄ {},

Κα΄α΄ α΄Κα΄ Ι΄α΄α΄‘ α΄ α΄Κ?Ιͺα΄α΄ ?α΄Κ Ι΄α΄xα΄ α΄ α΄ΚΙͺ?Ιͺα΄α΄α΄Ιͺα΄Ι΄,
α΄Ι΄α΄α΄Κ α΄Ι΄ΚΙͺα΄Ιͺα΄α΄α΄ α΄α΄α΄ Ιͺα΄κ± α΄Κ κ±α΄ΚΙͺα΄κ±...</b>"""

    VERIFY_TXT = """<b>Κα΄ΚΚα΄ {},

Κα΄α΄Κ α΄Κα΄ Ι΄α΄α΄ α΄ α΄ΚΙͺ?Ιͺα΄α΄ α΄α΄α΄α΄Κ,
α΄Κα΄α΄κ±α΄ α΄ α΄ΚΙͺ?Κ Ι΄α΄α΄‘ α΄Ι΄α΄ Ι’α΄α΄ α΄Ι΄ΚΙͺα΄Ιͺα΄α΄α΄ α΄α΄α΄α΄κ±κ± ?α΄Κ Ι΄α΄xα΄ α΄ α΄ΚΙͺ?Ιͺα΄α΄α΄Ιͺα΄Ι΄...

ΰ€ΰ€Έ ΰ€¬ΰ€Ύΰ₯ΰ€ ΰ€ΰ₯ ΰ€ΰ€Έΰ₯ΰ€€ΰ₯ΰ€?ΰ€Ύΰ€² ΰ€ΰ€°ΰ€¨ΰ₯ ΰ€ΰ₯ ΰ€²ΰ€Ώΰ€ ΰ€ΰ€ͺΰ€ΰ₯ α΄ α΄ΚΙͺ?Κ ΰ€ΰ€°ΰ€¨ΰ€Ύ ΰ€Ήΰ₯ΰ€ΰ€Ύ ΰ€¨ΰ€Ήΰ₯ΰ€ ΰ€€ΰ₯ ΰ€ΰ€ͺ ΰ€ΰ€Έΰ€ΰ€Ύ ΰ€ΰ€Έΰ₯ΰ€€ΰ₯ΰ€?ΰ€Ύΰ€² ΰ€¨ΰ€Ήΰ₯ΰ€ ΰ€ΰ€° ΰ€ͺΰ€Ύΰ€ΰ€ΰ€ΰ₯ |</b>"""

    VERIFY2_TXT = """
<b>#π΄π²π€π±_π΅π€π±π¨π₯π¨π€π£_π’π?π¬π―π«π€π³π€

π΄ππΎπ π­πΊππΎ : {} [ <code>{}</code> ]

π£πΊππΎ  : <code>{}</code></b>
"""
