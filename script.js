const 事情=document.querySelector(".文字欄");
const 清單=document.querySelector(".清單");
const 按鈕=document.querySelector(".按鈕");

function add(){
    if(事情.value=="") return;
    const eve=document.createElement("li");
    eve.innerHTML=`
    <input type="checkbox" class="打勾方塊">
    <label>${事情.value}</label>
    <button class="垃圾桶">🗑️</button>
    `
    const 垃圾桶=eve.querySelector(".垃圾桶");
    const 方塊=eve.querySelector(".打勾方塊");
    垃圾桶.addEventListener("click",function(){
        eve.remove();
    });
    方塊.addEventListener("change",function(){
        if(方塊.checked){
            eve.style.textDecoration="line-through";
            eve.style.color="#999";
            清單.append(eve);
        }
        else{
            eve.style.textDecoration="none";
            eve.style.color="";
            清單.prepend(eve);
        }
    });
    清單.append(eve);
    事情.value="";
}
事情.addEventListener("keyup",function(e){
    if(e.key=="Enter"){
        add();
    }
});
按鈕.addEventListener("click",add);