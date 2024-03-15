<?php      
ob_start();      
define('API_KEY','7116208895:AAGm_jAaxl5XryaViut3Z9nM1zKZDqDvYpM');//توكن بوت
  
/*غير الحقوق واثبت انك فاشل
اذا تريد تنقل اذكر اسمي او اسم قناتي */

/*====================
Make : @X_E_U_B
DEV : @X_E_U_B
Translator : Team Sonic
/*====================*/
function ACL($callbackQueryId, $text = null, $showAlert = false)
{        
     return bot('answerCallbackQuery', [        
        'callback_query_id' => $callbackQueryId,    
        'text' => $text,        
        'show_alert'=>$showAlert,        
    ]);        
}        
function get($fayl){     
$get = file_get_contents("$fayl");     
return $get;     
}     


function bot($method,$datas=[]){      
    $url = "https://api.telegram.org/bot".API_KEY."/".$method;
    $ch = curl_init();      
    curl_setopt($ch,CURLOPT_URL,$url);      
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
    curl_setopt($ch,CURLOPT_POSTFIELDS,$datas);
    $res = curl_exec($ch);      
    if(curl_error($ch)){      
        var_dump(curl_error($ch));      
    }else{      
        return json_decode($res);      
    }      
}      
$update = json_decode(file_get_contents('php://input'));
$uid = $message->from->id;       
$cid = $message->chat->id;       
$edname = $editm ->from->first_name;      
$message = $update->message;      
$ncm = $message->new_chat_member->id;      
$mid = $message->message_id;      
$chat_id = $message->chat->id;      
$mtext = $message->text;      
$forward = $update->message->forward_from;     
$from_user_first_name = $message->reply_to_message->from->first_name;    

$editm = $update->edited_message;      
$fadmin = $message->from->id;      
$cidtyp = $message->chat->type;        
$tx = $message->text;        
$callback = $update->callback_query;        
$mmid = $callback->inline_message_id;        
$mes = $callback->message;        
$cmtx = $mes->text;        
$mmid = $callback->inline_message_id;        
$idd = $callback->message->chat->id;        
$cbid = $callback->from->id;        
$data = $update->callback_query->data;      
$cid2 = $update->callback_query->message->chat->id;      
$mid2 = $update->callback_query->message->message_id;      
$ida = $callback->id;        
$cqid = $update->callback_query->id;        
$name = $message->from->first_name;           
$cty = $message->chat->type;      
$tgg = $message->reply_to_message->from->first_name;      
$tfuu = $message->reply_to_message->message_id;       
$step = file_get_contents("mrax/$chat_id.step"); 
mkdir("mrax");      

$baza = file_get_contents("mrax.dat");     
$baza1 = substr_count($baza,"\n");     
$gruppa = substr_count($baza,"-");     
$odam = $baza1 - $gruppa;     
$til1 = file_get_contents("mrax/$chat_id.txt");   
$til = file_get_contents("mrax/$cid2.txt");   

//cid2 uchun    
if($til == "uz") {   
$khelp = "اوامر البوت";  
$help = "*سيقوم هذا الروبوت بتنفيذ المهام التالية فقط إذا كنت مسؤولاً في المجموعة*

أوامر لمشرفي المجموعة  

/kick - الطرد من المجموعة ⚠️ 
/ban - يمنعك من الانضمام مرة أخرى إلى المجموعة
/mute - لن أكتب في المجموعة لمدة 3 ساعات
/unmute - ازلة الكتم من شخص  ";  
$stat = "*إحصائيات*📈    
⭐️*$odam* الاشخاص    
🚸 *$gruppa* جروبات      

✅المجموع الكلي *$baza1*";   
$sta = "إحصائيات";   
$bot = "معلومات";   
$sokin = "الصمت في المجموعة";   
$banne = "سأحظره إذا عاد مرة أخرى⚠️";   
$bot1 = "*هذا هو الغرض من إنشاء الروبوت*   

_هذا البوت هو بالفعل بوت دولي ويعمل في جميع أنحاء العالم !! الغرض من إنشاء هذا الروبوت هو مساعدة مسؤولي المجموعات المختلفة kanalimiz @O_1_W_";
$upda = "تحديث ♻️";   
$unmute = "وفي حالة إرجاعه مرة أخرى سيتم حظرك😠";  
$tang = "اختر القائمة ✋️";  
$minyu = "بدء 📮";   
$obot = "معلومات ";  
$inline = "*هذا البوت هو بالفعل بوت دولي ويعمل في جميع أنحاء العالم !! الغرض من إنشاء هذا الروبوت هو مساعدة مسؤولي المجموعات المختلفة*

🇪🇬 مبرمج البوت [@X_E_U_B]";  
}   

if($til == "rus") {   
$help = "*Если кто-то в группе будет материться, то лично бот наказывает этого профиля!*

Команды для админов группы !!   
/kick - Если надо кого то изгнать из группы то аоспользуйтесь этой командой ⚠️
/ban - Команда для бана пользователя   
/mute - Режим RO [( RO read only  спомощью этой команды пользователь попадает в тихий режим)]
/unmute - Убирает режим *RO*";   
$stat = "*Статистика*📈    
⭐️*$odam* участников бота    
🚸 *$gruppa* группы      

✅*$baza1* Всего";   
$sta = "Статистика";   
$bot = "о боте";   
$bot1 = "Этот бот  - международный бот, и он работает во всем мире!
Цель создания этого бота заключалась в том, чтобы помочь администраторам группы";
$upda = "обновить ♻️";   
$menyu = "Главный меню 📮";   
$khelp = "Помочь";  
$tang = "Выберите ✋️";  
$obot = "О боте";  
$inline = "*Этот бот  - международный бот, и он работает во всем мире!
Цель создания этого бота заключалась в том, чтобы помочь администраторам группы*

🇪🇬 Разработчики [@X_E_U_B]";  
}   

// chat id uchun   
if($til1 == "uz") {   
$unmute = "$from_user_first_name وفي حالة إرجاعه مرة أخرى سيتم حظرك😠"; 
$kick = "تم طرد الخول 👍";   
$mute = "تم كتم مستخدم";  
$obot = "حول البوت ";  
$inline = "*هذا البوت هو بالفعل بوت دولي ويعمل في جميع أنحاء العالم !! الغرض من إنشاء هذا الروبوت هو مساعدة مسؤولي المجموعات المختلفة*

🇪🇬 مبرمج البوت [@X_E_U_B]";  
$welcome = "تريد تڪبر خخاوينا. 𝁫🎄
 ‌

 منحتاج تـفـا؏ـل ونستنا وضحڪטּﭑ 𝁫𓆩💞𓆪𝁫 
  يڪون تفا؏ـلنا .𝁫𓆩 💞 𓆪𝁫

Link :-😕"; 
}   
if($til1 == "rus") {   
$banne = "Повторите эту ошибку еще раз вы получаете бан😠";   
$unmute = "$from_user_first_name Ещё повториться я дам тебе бан 😠";
$kick = "Кикнул 👨‍✈️";   
$mute = "Он в Режиме *RO*";  
$obot = "О боте";  
$inline = "*Этот бот  - международный бот, и он работает во всем мире!
Цель создания этого бота заключалась в том, чтобы помочь администраторам группы*

🇪🇬 Разработчики [@X_E_U_B]";  
$welcome = "добро пожаловать "; 
}   

if((mb_stripos($mtext,"/start")!==false) or ($mtext == "/set_lang@SP0Z_BOT")) {
  bot('sendmessage',[       
   'chat_id'=>$chat_id,       
     'parse_mode'=>'markdown',       
   'text'=>"_اهلا بك عزيزى فى بوت الحماية اختر لغة الخاصة بك 🇪🇬 🇷🇺_",       
  'reply_markup'=>json_encode([       
   'inline_keyboard'=>[       
       [['text'=>"عربية 🇪🇬", 'callback_data' => "uz"],['text'=>"Русский 🇷🇺", 'callback_data' => "ru"]]    
]       
])       
]);     
$baza = file_get_contents("mrax.dat");     
if(mb_stripos($baza, $chat_id) !== false){     
}else{     
file_put_contents("mrax.dat", "$baza\n$chat_id");
}     
}       

if($data == "ru"){       
file_put_contents("mrax/$cid2.txt","rus");   
bot('sendMessage',[     
     'chat_id'=>$cid2,     
     'text'=>"*Ураа Русский язык 🤹🏻‍♂️*    
_Разработка_ 👌 [@X_E_U_B]",     
     'parse_mode'=>'markdown',     
  'reply_markup'=>json_encode([       
   'inline_keyboard'=>[       
              [['text'=>"Главный меню 📮", 'callback_data' => "menyu"]]
]       
])       
]);      
}       

if($data == "uz"){       
file_put_contents("mrax/$cid2.txt","uz");   
bot('sendMessage',[     
     'chat_id'=>$cid2,     
     'text'=>"*اهلا بك فى لغة العربية اضغط على زر البدء😜*    
مبرمج البوت 👌 [@X_E_U_B]",     
     'parse_mode'=>'markdown',     
  'reply_markup'=>json_encode([       
   'inline_keyboard'=>[       
       [['text'=>"بدء 📮", 'callback_data' => "menyu"]]
]       
])       
]);      
}       

if($data == "help"){       
bot('sendMessage',[     
     'chat_id'=>$cid2,     
     'text'=>$help,    
     'parse_mode'=>'markdown',     
  'reply_markup'=>json_encode([       
   'inline_keyboard'=>[       
       [['text'=>"$sta 📈", 'callback_data' => "stat"],['text'=>" $bot 🤖", 'callback_data'=>"bot"]]   
]       
])       
]);      
}       
//إحصائيات     

if($data == "stat"){     
bot('sendMessage',[     
     'chat_id'=>$cid2,     
     'text'=>$stat,     
     'parse_mode'=>'markdown',     
  'reply_markup'=>json_encode([       
   'inline_keyboard'=>[       
       [['text'=>"$upda", 'callback_data' => "stat"]]  
]       
])       
]);      
}       
$fadmin = $message->from->id;    
if((mb_strpos($mtext, 'сука')!==false) or ($mtext == "гандон") or ($mtext == "нахуй") or ($mtext == "жопа") or ($mtext == "пидер") or ($mtext == "am") or ($mtext == "am" )or ($mtext == "kot") or ($mtext == "yalaq") or ($mtext == "suka") or ($mtext == "san") or ($mtext == "Dux") or ($mtext == "dnx") or ($mtext == "DNX") or ($mtext == "itaraman")) {
  bot('sendmessage',[    
    'chat_id'=>$chat_id,    
    'text'=>$sokin,   
  ]);    
  $minut = strtotime("+ 180 m");    
  bot('restrictChatMember',[    
    'chat_id'=>$chat_id,    
    'user_id'=>$fadmin,    
    'until_date'=>strtotime("+ 180 minutes "), 
  ]);    
}    

$id = $message->reply_to_message->from->id;   
if((mb_stripos($mtext,"/kick")!==false) or ($mtext == "/kick@SP0Z_BOT")) {
if($cty == "supergroup" or $cty == "group"){ 
$gett = bot('getChatMember', [ 
'chat_id' =>$chat_id, 
'user_id' =>$message->from->id, 
]); 
$get = $gett->result->status; 
if($get =="admin" or $get == "creator"){ 
    bot('kickChatMember', [   
        'chat_id' => $chat_id,   
        'user_id' => $id,   
        'can_send_messages' => false,   
        'can_send_media_messages' => false,   
        'can_send_other_messages' => false,   
        'can_add_web_page_previews' => false   
    ]);   
    bot('sendMessage', [   
        'chat_id'=>$chat_id,   
        'text'=>$kick,   
    ]);   
  }   
} 
} 


if((mb_stripos($mtext,"/ban")!==false) or ($mtext == "/ban@Soursevip38bot")) {
    bot('kickChatMember', [   
        'chat_id'=>$chat_id,   
        'user_id'=>$message->from->id, 
        'can_send_messages' => false,   
        'can_send_media_messages' => false,   
        'can_send_other_messages' => false,   
        'can_add_web_page_previews' => false   
    ]);   
  }   

if($data == "bot"){     
bot('sendMessage',[    
     'chat_id'=>$cid2,    
     'text'=>$bot1,   
     'parse_mode'=>'markdown',    
  'reply_markup'=>json_encode([      
   'inline_keyboard'=>[      
       [['text'=>"$menyu", 'callback_data' => "menyu"]]
]      
])      
]);     
}   

if($data == "menyu"){     
bot('sendMessage',[    
     'chat_id'=>$cid2,    
     'text'=>$tang,   
     'parse_mode'=>'markdown',    
  'reply_markup'=>json_encode([      
   'inline_keyboard'=>[      
       [['text'=>"$sta 📈", 'callback_data' => "stat"],['text'=>" $bot 🤖", 'callback_data'=>"bot"]],  
              [['text'=>"$khelp 📨", 'callback_data' => "help"]]
]      
])      
]);     
}   

if(mb_stripos($mtext, "/unmute")!==false){  
if($cty == "supergroup" or $cty == "group"){ 
$gett = bot('getChatMember', [ 
'chat_id' =>$chat_id, 
'user_id' =>$message->from->id, 
]); 
$get = $gett->result->status; 
if($get =="admin" or $get == "creator"){ 
  bot('restrictChatMember',[    
    'chat_id'=>$chat_id,    
    'user_id'=>$message->from->id, 
    'can_send_messages'=>true,    
    'can_send_media_messages'=>true,    
    'can_send_other_messages'=>true,    
    'can_add_web_page_previews'=>true    
  ]);    
  bot('sendChatAction',['chat_id'=>$chat_id,'action'=>"typing"]);    
  bot('sendmessage',[    
    'chat_id'=>$chat_id,    
 'parse_mode'=>'html',   
    'text'=>$unmute, 
  ]);    
}    
} 
} 

if(mb_stripos($mtext, "/mute")!==false){  
$tek = bot('getChatMember', [ 
'chat_id' => $chat_id, 
'user_id' =>$message->from->id, 
]); 
$get = $tek->result->status; 
if($get =="administrator" or $get == "creator"){ 
  bot('restrictChatMember',[    
    'chat_id'=>$chat_id,    
    'user_id'=>$id,    
  ]);    
  bot('sendChatAction',['chat_id'=>$chat_id,'action'=>"typing"]);    
  bot('sendmessage',[    
    'chat_id'=>$chat_id,    
    'parse_mode'=>'markdown',   
    'text'=>$mute,   
  ]);    
}  
} 

if(isset($update->inline_query)){  
$userID = $update->inline_query->from->id;  
$theQuery = $update->inline_query->query;  
$cid = $update->inline_query->query;  
if(mb_stripos("0")!==false){  
$cid = str_replace("o","",$cid);  
bot('answerInlineQuery', [  
'inline_query_id'=>$update->inline_query->id,  
'cache_time'=>2,  
'results'=>json_encode([[  
'type'=>'article',  
'id'=>base64_encode(1),  
'title'=>"حول البوت",  
'input_message_content'=>[  
'disable_web_page_preview'=>true,  
'parse_mode' => 'markdown',  
'message_text'=>"_هذا هو الغرض من إنشاء الروبوت_  

*هذا البوت هو بالفعل بوت دولي ويعمل في جميع أنحاء العالم !! الغرض من إنشاء هذا الروبوت هو مساعدة مسؤولي المجموعات المختلفة*

🇪🇬 مبرمج البوت [@X_E_U_B]"],  
]])  
]);  
}  
} 

if($mtext == "/welcome"){   
bot('sendmessage',[   
'chat_id'=>$chat_id,   
'text'=>$welcome,  
'parse_mode'=>"markdown",   
'reply_markup'=>$bekor,   
]);   
}   



// الترحيب
elseif(isset($update->message-> left_chat_member )){ 
    $name = $message->from->first_name; 
bot('sendMessage',[ 
      'chat_id'=>$chat_id, 
      'reply_to_message_id'=>$mesid, 
'text'=>$hayr, 
    ]); 
}
Make By Team Sonic

/*====================
CH : @X_E_U_B
DEV : @X_E_U_B
Translator : Team Sonic
/*====================*/