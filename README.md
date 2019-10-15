最近面试了不少公司，正好把记得的问题做个总结。

本文 [github](https://github.com/sushengbuhuo/php-interview-2018) 会持续更新 

本文[sf](https://segmentfault.com/a/1190000015651120)

欢迎关注公众号：苏生不惑  每周更新文章，一个有趣又有用的公众号

![关注](https://mmbiz.qpic.cn/mmbiz_jpg/sZeVtjGD4lFg1Ijxp4V5UfVuOkP90u1H3Ifm02J5ibEdoTsvpavaSGO2tGBrH2fxUibI8uiclUo0QrFguhfjnialbw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

# 简历

关于简历怎么写，知乎上有很多对应问题，可以自行搜索，这里推荐几个简历相关的 repo

[程序员写简历时，常用的例句范式]( https://github.com/resumejob/awesome-resume)

[简历常用例句 ](https://github.com/resumejob/awesome-resume) 

[程序员简历模板](https://github.com/geekcompany/ResumeSample )

[在线简历]( http://cv.ftqq.com/#)

[md简历](https://resume.mdnice.com/)

# 笔试题

### 写一个email的正则
```js
$mail = 'test@sina.com';  //邮箱地址
$pattern = "/^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$/";
preg_match($pattern, $mail, $matches);
//验证可以使用 filter_var($email, FILTER_VALIDATE_EMAIL)
```
### 关系比较 
[参考官网](http://php.net/manual/zh/types.comparisons.php)

![clipboard.png](https://segmentfault.com/img/bVbdOqw?w=835&h=497)

### echo (int)((0.1+0.7)*10);//7
看似有穷的小数, 在计算机的二进制表示里却是无穷的 http://www.cnblogs.com/datang6777/p/7049159.html 
echo serialize(0.1+0.7); //d:0.79999999999999993;

### 熟悉的linux命令
ps cat tail top awk

### javascript跨域如何实现
jsonp 和 cors

### 熟悉的5种设计模式及用单例模式建立一个数据库连接
单例 工厂 策略 适配器 观察者
```js
<?php
//参考 https://www.cnblogs.com/Steven-shi/p/5858229.html 
class DBHelper
{
    private $link;
    static private $_instance;

    // 连接数据库
    private function __construct($host, $username, $password)
    {
        $this->link = mysql_connect($host, $username, $password);
        $this->query("SET NAMES 'utf8'", $this->link);
        //echo mysql_errno($this->link) . ": " . mysql_error($link). "n";
        //var_dump($this->link);
        return $this->link;
    }
    private function __clone()
    {
    }
    public static function get_class_nmdb($host, $username, $password)
    {
        //$connector = new nmdb($host, $username, $password);
        //return $connector;

        if (FALSE == (self::$_instance instanceof self)) {
            self::$_instance = new self($host, $username, $password);
        }
        return self::$_instance;
    }
    // 连接数据表
    public function select_db($database)
    {
        $this->result = mysql_select_db($database);
        return $this->result;
    }
    // 执行SQL语句
    public function query($query)
    {
        return $this->result = mysql_query($query, $this->link);
    }
    // 将结果集保存为数组
    public function fetch_array($fetch_array)
    {
        return $this->result = mysql_fetch_array($fetch_array, MYSQL_ASSOC);
    }
    // 获得记录数目
    public function num_rows($query)
    {
        return $this->result = mysql_num_rows($query);
    }
    // 关闭数据库连接
    public function close()
    {
        return $this->result = mysql_close($this->link);
    }
}
$connector = DBHelper::get_class_nmdb($host, $username, $password);
$connector -> select_db($database);
?>
```
### 冒泡排序 大数在前 小数在后
```js
$arr=[5,2,8,1,9];
$len=count($arr);
for($k=1;$k<$len;$k++)
{
    for($j=0;$j<$len-$k;$j++){
        if($arr[$j]<$arr[$j+1]){
            list($arr[$j+1],$arr[$j])=[$arr[$j],$arr[$j+1]];
            
        }
    }
}
print_r($arr);
```
### 如何实现单点登录
利用 jwt 实现 session 共享，具体使用 jwt 参考 http://blog.leapoahead.com/2015/09/07/user-authentication-with-jwt/ 
### 出现性能瓶颈如何快速定位解决
服务器负载 慢日志 xhprof 慢sql
### 熟悉的 nosql 和 sql 有什么区别（优势，劣势）
 Memcache，Redis 都是内存数据库 
redis是一个开源的支持多种数据类型的key=>value的存储数据库。支持字符串、列表、集合、有序集合、哈希五种类型
memcache 只支持简单的key/value数据结构，不像Redis可以支持丰富的数据类型。
 无法进行持久化，数据不能备份，只能用于缓存使用，且重启后数据全部丢失

### 如何保证代码质量
高质量代码三要素：可读性，可维护性，可变更性 代码质量评价：低耦合，高内聚  https://segmentfault.com/a/1190000004355331 

### 学习PHP的渠道 看过的PHP书，了解的PHP开源项目 
php.net sf google 
《Modern PHP》《PHP核心技术和最佳实践》《PHP the right way》
laravel carbon querylist等

### mysql innodb 有哪些索引类型 分别在什么场景下使用
索引的本质还是提升查询数据库的速度，减少服务器I/O开销 
主键 唯一 普通 联合 

### 对一个链表顺序反转

### 实现PHP5中的 var_dump 函数
```js
function mydump() {
        $args   = func_num_args();
        for($i = 0;$i < $args; $i ++) {
            $param = func_get_arg($i);
            switch(gettype($param)) {
                case 'NULL' :
                    echo 'NULL';
                    break;
                case 'boolean' :
                    echo ($param ? 'bool(true)' : 'bool(false)');
                    break;
                case 'integer' :
                    echo "int($param)";
                    break;
                case 'double' :
                    echo "float($param)";
                    break;
                case 'string' :
                    dumpString($param);
                    break;
                case 'array' :
                    dumpArr($param);
                    break;
                case 'object' :
                    dumpObj($param);
                    break;
                case 'resource' :
                    echo 'resource';
                    break;
                default :
                    echo 'UNKNOWN TYPE';
                    break;
            }
        }
    }
 
 
function dumpString($param) {
    $str = sprintf("string(%d) %s",strlen($param),$param);
    echo $str;
}
 
function dumpArr($param) {
    $len = count($param);
    echo "array($len) {\r\n";
    foreach($param as $key=>$val) {
        if(is_array($val)) {
            dumpArr($val);
        } else {
            echo sprintf('["%s"] => %s(%s)',$key,gettype($val),$val);
        }
    }
    echo "}\r\n";
}
 
function dumpObj($param) {
    $className = get_class($param);
    $reflect = new ReflectionClass($param);
    $prop = $reflect->getDefaultProperties();
    echo sprintf("Object %s #1(%d) {\r\n",$className,count($prop));
    foreach($prop as $key=>$val) {
        echo "[\"$key\"] => ";
        mydump($val);
    }
    echo "}";
}
 
class MyClass
{
    protected $_name;
    function test()
    {
        echo "hello";
    }
}
 
$str    = "test";
mydump(new MyClass(),$str);
echo "\r\n";
$arr2   = array(
    "1"     => "Ddaddad",
    "one"   => array("two" => "Dddd" ),
    "three" => 1
);
mydump($arr2); 
mydump(1,true,null);
```
### 如何设计一个微博
用户可以关注他人 可以发布微博 可以查看关注人的微博 可以评论微博

用户表 关注表 微博表 评论表 

### 获取上周一和周日的日期
`echo date('Y-m-d',strtotime('monday last week'));`
`echo date('Y-m-d', strtotime('-' . (6+date('w')) . ' days'));`
`echo date('Y-m-d',strtotime('sunday last week'));`
### 对数组实现去除空元素 排重 按值从大到小排序 重新建立数字索引 
`array_values(rsort(array_unique(array_filter($arr))))`
### 对二维数组按照 title+pubscore 去重
```js
function unique_by_key($arr, $key1,$key2) {
  $tmp_key = [];
  foreach ($arr as $key => $item) {
      if ( in_array($item[$key1].$item[$key2], $tmp_key) ) {
        unset($arr[$key]);
      } else {
        $tmp_key[] = $item[$key1].$item[$key2];
    }
  }
  return $arr;
}
//使用示例：
$arr = array(
  array('id' => 1, 'title' => 'a','pubscore'=>1),
  array('id' => 2, 'title' => 'a','pubscore'=>1),
  array('id' => 3, 'title' => 'b','pubscore'=>2),
  array('id' => 4, 'title' => 'c','pubscore'=>3),
  array('id' => 5, 'title' => 'd','pubscore'=>3),
);
print_r(unique_by_key($arr,'title','num'));

```
### 写一个正则 匹配新闻标题不能为数字，纯字母，不能包含 彩票/广告/启示

### linux 压缩 解压缩命令
`tar -cvf jpg.tar *.jpg`
`tar -xvf jpg.tar`
### linux下后台执行 test.php 将结果输出到test.log
`php test.php & >test.log`
### 写一个shell命令 实现找出所有包含 spread的进程，杀死这些进程并记录日志，日志包含杀死进程名称和杀死进程的时间
`ps -ef |grep spread |grep -v grep |awk '{print $2}'|xargs kill -9`
`kill -9 $(ps -ef | grep spread| grep -v grep | awk '{print $2}')`
### 一个json 转化输出有层级的文本
参考 https://segmentfault.com/a/1190000008265618
### 排行榜统计 sql 
订单表有如下字段
id 自增id
user_id 购买者id
product_id 商品id
time 购买时间
price 订单总价
找出销量大于1000的商品，按销量倒序 和 找出消费最多的10个用户

`select product_id,count(*) s from orders group by product_id order by s  having s>1000;`

`select user_id,sum(price) s from orders group by user_id order by s desc limit 10;`

### 列出你知道的魔术方法 ，并说明他们的用途

[参考手册](http://php.net/manual/zh/language.oop5.magic.php)

### 写出你知道的http头部属性 注意大小写 并说明用途
```js
Accept	指定客户端能够接收的内容类型	Accept: text/plain, text/html
Accept-Charset	浏览器可以接受的字符编码集。	Accept-Charset: iso-8859-5
Accept-Encoding	指定浏览器可以支持的web服务器返回内容压缩编码类型。	Accept-Encoding: compress, gzip
Accept-Language	浏览器可接受的语言	Accept-Language: en,zh
Accept-Ranges	可以请求网页实体的一个或者多个子范围字段	Accept-Ranges: bytes
Authorization	HTTP授权的授权证书	Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==
Cache-Control	指定请求和响应遵循的缓存机制	Cache-Control: no-cache
Connection	表示是否需要持久连接。（HTTP 1.1默认进行持久连接）	Connection: close
Cookie	HTTP请求发送时，会把保存在该请求域名下的所有cookie值一起发送给web服务器。	Cookie: $Version=1; Skin=new;
Content-Length	请求的内容长度	Content-Length: 348
Content-Type	请求的与实体对应的MIME信息	Content-Type: application/x-www-form-urlencoded
Date	请求发送的日期和时间	Date: Tue, 15 Nov 2010 08:12:31 GMT
Expect	请求的特定的服务器行为	Expect: 100-continue
From	发出请求的用户的Email	From: user@email.com
Host	指定请求的服务器的域名和端口号	Host: www.zcmhi.com
If-Match	只有请求内容与实体相匹配才有效	If-Match: “737060cd8c284d8af7ad3082f209582d”
If-Modified-Since	如果请求的部分在指定时间之后被修改则请求成功，未被修改则返回304代码	If-Modified-Since: Sat, 29 Oct 2010 19:43:31 GMT
If-None-Match	如果内容未改变返回304代码，参数为服务器先前发送的Etag，与服务器回应的Etag比较判断是否改变	If-None-Match: “737060cd8c284d8af7ad3082f209582d”
If-Range	如果实体未改变，服务器发送客户端丢失的部分，否则发送整个实体。参数也为Etag	If-Range: “737060cd8c284d8af7ad3082f209582d”
If-Unmodified-Since	只在实体在指定时间之后未被修改才请求成功	If-Unmodified-Since: Sat, 29 Oct 2010 19:43:31 GMT
Max-Forwards	限制信息通过代理和网关传送的时间	Max-Forwards: 10
Pragma	用来包含实现特定的指令	Pragma: no-cache
Proxy-Authorization	连接到代理的授权证书	Proxy-Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==
Range	只请求实体的一部分，指定范围	Range: bytes=500-999
Referer	先前网页的地址，当前请求网页紧随其后,即来路	Referer: http://www.zcmhi.com/archives/71.html
TE	客户端愿意接受的传输编码，并通知服务器接受接受尾加头信息	TE: trailers,deflate;q=0.5
Upgrade	向服务器指定某种传输协议以便服务器进行转换（如果支持）	Upgrade: HTTP/2.0, SHTTP/1.3, IRC/6.9, RTA/x11
User-Agent	User-Agent的内容包含发出请求的用户信息	User-Agent: Mozilla/5.0 (Linux; X11)
Via	通知中间网关或代理服务器地址，通信协议	Via: 1.0 fred, 1.1 nowhere.com (Apache/1.1)
Warning	关于消息实体的警告信息	Warn: 199 Miscellaneous warning
```
### 有一个文本文件，内容为ip 每行一个ip 格式为 
1.2.3.4 
4.5.6.7
2.3.4.5
1.2.3.4
写出 shell命令 统计 ip出现的次数 结果类似
1.2.3.4 2
4.5.6.7  1
2.3.4.5  1

`awk '{arr[$1]++;}END{for(i in arr){print i , arr[i] }}' test.txt`
### __destruction() 和 __autoload()触发时机
unset 和 加载一个为包含的文件
### 如何实现一个数组[1,2,3]连续复制3次变为[1,2,3,1,2,3,1,2,3]
```js
$arr=[1,2,3];
print_r(f($arr,3));
function f($arr,$num){
    return array_filter(explode(',',str_repeat(implode(',',$arr).',',$num)));
}
```
 
### 抽象类和接口的区别，分别在什么场景使用
抽象类可以实现的功能，接口也可以实现。
抽象类的接口的区别，不在于编程实现，而在于程序设计模式的不同。
一般来讲，抽象用于不同的事物，而接口用于事物的行为。
参考 https://segmentfault.com/a/1190000004699158 

### 猴子选大王 
一群猴子排成一圈，按1，2，...，n依次编号。然后从第1只开始数，数到第m只,把它踢出圈，从它后面再开始数，再数到第m只，在把它踢出去...，如此不停的进行下去，直到最后只剩下一只猴子为止，那只猴子就叫做大王。要求编程模拟此过程，输入m、n,输出最后那个大王的编号
```js
echo monkey(10,4);//5
function monkey($m,$n){
    $arr=range(1,$m);
    $i=0;
    while(count($arr)>1){
        if(($i+1)%$n==0){
            unset($arr[$i]);
        }else{
            $arr[]=$arr[$i];
            unset($arr[$i]);
        }
        $i++;
    }
    return $arr[$i];
}
```
### 写一个快速排序
```js
function quickSort($arr) {
    $len = count($arr);
    if($len <= 1) {
        return $arr;
    }

    $base = $min = $max = [];

    $base_item = $arr[0];

    for($i = 0; $i < $len ; $i++) {
        if($arr[$i] < $base_item) {
            $min[] = $arr[$i];
        }elseif($arr[$i] > $base_item) {
            $max[] = $arr[$i];
        }else {
            $base[] = $arr[$i];
        }
    }

    $min = quickSort($min);
    $max = quickSort($max);
    return array_merge($min,$base,$max);
}
```
### 实现一个发红包功能，100元发给8人

### 实现斐波那契数列
```js

function fib($n) {
    if($n <= 0) return 0;
    if ($n <= 2) return 1;
    return fib($n - 1) + fib($n - 2);
} 
 
function fib2($n) {
if ($n <= 2) return 1;
$arr = [0,1,1];
for ($i = 3; $i <= $n; $i++) {
    $arr[$i] = $arr[$i - 1] + $arr[$i - 2];
}
return $arr[$n];
} 
```
### 二分查找
```js
function binSearch($arr,$search){
$height=count($arr)-1;
$low=0;
while($low<=$height){
$mid=floor(($low+$height)/2);//获取中间数
if($arr[$mid]==$search){
return $mid;
}elseif($arr[$mid]<$search){//当中间值小于所查值时，则$mid左边的值都小于$search，此时要将$mid赋值给$low
$low=$mid+1;
}elseif($arr[$mid]>$search){//中间值大于所查值,则$mid右边的所有值都大于$search,此时要将$mid赋值给$height
$height=$mid-1;
}
}
return "查找失败";
}
```
### 二维数组转换成一维数组
```js
$user = array(
     array('id' => 100, 'username' => 'a1'),
     array('id' => 101, 'username' => 'a2'),
     array('id' => 102, 'username' => 'a3'),
     array('id' => 103, 'username' => 'a4'),
     array('id' => 104, 'username' => 'a5'),
);
$result = array_reduce($user, function ($result, $value) {
    return array_merge($result, array_values($value));
}, array());
/*
Array
(
    [0] => 100
    [1] => a1
    [2] => 101
    [3] => a2
    [4] => 102
    [5] => a3
    [6] => 103
    [7] => a4
    [8] => 104
    [9] => a5
)
*/
$result = [];
array_walk_recursive($user, function($value) use (&$result) {
    array_push($result, $value);
});
$result = [];
array_map(function ($value) use (&$result) {
    $result = array_merge($result, array_values($value));
}, $user);
```
### 2次foreach 输出什么
```js
//参考https://segmentfault.com/q/1010000008279730
$arr = [1,2,3];
    foreach($arr as &$v) {
        //nothing todo.
    }
    foreach($arr as $v) {
        //nothing todo.
    }
    var_export($arr);
    //output:array(0=>1,1=>2,2=>2)
 ```
# 面试题

### nginx 热启动
nginx -s reload

### 读取1G大文件
使用游标或者yield生成器来获取数据库的数据  https://segmentfault.com/a/1190000012334856

### http  https 区别 
 HTTPS协议是由SSL+HTTP协议构建的可进行加密传输、身份认证的网络协议，要比http协议安全。 参考 https://www.itcodemonkey.com/article/4195.html 

### redis 持久化
 aof rdb  http://www.hoohack.me/2018/04/04/deep-learning-redis-durability 
https://juejin.im/entry/5b35ad87f265da597759804b/ 
### 权限如何设计
user用户表、role角色表、perm权限表、role-user用户角色关联表、role-perm角色权限关联表
### apache nginx 区别
https://juejin.im/entry/5b34b2d7e51d4558ae19f2eb 
nginx从入门到实践 https://juejin.im/post/5a2600bdf265da432b4aaaba
### 数据库锁的了解
乐观锁（代码处理）与悲观锁( select for update) http://www.hollischuang.com/archives/934

### 2038 时间问题
```js
 //解决：DateTime 或者 使用64位操作系统

$str_time = '2100-10-02'; 
 function newStrToTime($str_time) { 
$result = strtotime($str_time);
if(empty($result)) { 
$date = new DateTime($str_time); 
$result = $date->format('U'); 
} 
return $result; 
} 
```
### 谈谈最近微信支付 xxe 漏洞
php 调用simplexml_load_string之前把外部引用实体关掉：  
libxml_disable_entity_loader(true);  
$data = json_decode(json_encode(simplexml_load_string($xml, 'SimpleXMLElement', LIBXML_NOCDATA)), true);

### 写个定时任务
`*　　*　　*　　*　　*　 command`     
分　时　日　月　周　命令 
工具 https://crontab-generator.org/ 
https://crontab.guru/   
https://tool.lu/crontab/
 https://atool.vip/crontab
### opcache了解
缓存字节码 
### array_merge + 区别 
[参考](https://segmentfault.com/a/1190000014838713)
### 如何实现多继承

trait的出现就是一种解决需要多继承场景的方式。 使用场景是如果多个类都要用到同样的属性或者方法，这个时候使用Traits可以方便的给类增加这些属性或方法，而不用每个类都去继承一个类，如果说继承类是竖向扩展一个类，那么Traits是横向扩展一个类，从而实现代码复用。 
 
[PHP中Trait详解及其应用]( https://segmentfault.com/a/1190000008009455 )

### PHP 多线程
 https://www.cnblogs.com/kluan/p/5934228.html 
https://www.cnblogs.com/zhenbianshu/p/7978835.html
```js
class Request extends Thread {
    public $url;
    public $response;
    public function __construct($url) {
        $this->url = $url;
    }
    public function run() {
        $this->response = file_get_contents($this->url);
    }
}
$ch = new Request("www.baidu.com");
$ch ->start();
```
### php执行流程 
浏览器输入URL->Nginx(从配置文件中加载nginx的fast-cgi模块)->php-fpm(fastcgi的进程管理器)
先到php-fpm的master进程(负责监听端口,接收Nginx的请求,据子进程的状态将请求分配给子进程去处理)->worker进程负责处理请求
worker 进程则一般有多个(具体数量根据实际需要配置)，每个进程内部都嵌入了一个 PHP 解释器，是 PHP 代码真正执行的地方。
 master 进程做的事情是 PHP环境初始化、事件监听(重启/重载、关闭、分发请求)、子进程状态
https://youngperson.github.io/blog/#/posts/16
### 如何优化 mysql 
### 如何防 SQL 注入
1 表单尽量用 post 提交,核心用户验证都走 post,避开 get容易暴露客户数据
2 使用HTTP_REFERER 检查源文件是否来自本系统
3 开启addslashes在特殊符号前加\
4 使用htmlspecialchars对字符串转实体
5 用户授权登录
6 使用PDO

数据库字段冗余，增添索引、优化sql、分库分表 主从分离  
### 常用 git 命令
git add git log git pull git push  git remote git checkout 
### php7常用新特性
比如标量类型声明、返回类型声明
### 自动加载如何实现的
spl_autoload_register composer
### 用过哪些PHP扩展
curl mb 
### php 异步如何实现
curl_multi_exec 
### 了解的微服务

### redis 过期如何处理
惰性删除与定期删除
### explain 关注哪些
type 字段 const、eq_reg、ref、range、index和ALL
### 对你最有挑战的项目是怎样的

### laravel 优势是什么
# 非技术问题
为什么从上家公司离职？
未来三年的职业规划的怎样的？
你有什么问的？

# 资源 

[PHP面试准备]( https://github.com/xianyunyh/PHP-Interview)

[关于面试/谈Offer/程序员职场生涯等]( https://github.com/lietoumai/awesome-offer)

[少写PHP "烂"代码](https://segmentfault.com/a/1190000015274515) 

[PHP工程师面试题目]( https://github.com/hookover/php-engineer-interview-questions)

[PHPer 面试指南](https://github.com/todayqq/PHPerInterviewGuide )

[一个16年毕业生所经历的php面试](https://github.com/OMGZui/noteBook/blob/master/level.md)

[找工作遇到的面试题目]( https://cloud.tencent.com/developer/article/1104156 )

[大话编程]( https://mp.weixin.qq.com/s/nCx7Jb5WRXGzkpsuth6LAw) 

https://mp.weixin.qq.com/s/13OJ8YAXLj3tqAC0aZ1e_Q

[strace帮助你调试PHP代码]( https://www.jianshu.com/p/cbc716f8a932? )

[Resetful API 设计规范](https://godruoyi.com/posts/the-resetful-api-design-specification )

[Java 基础知识、底层原理 面试]( https://github.com/crossoverJie/Java-Interview)

[PHP基础数据结构专题系列目录地址](https://github.com/xx19941215/light-tips)

[后端架构师技术图谱]( https://github.com/xingshaocheng/architect-awesome)

[记一次面试，分享我整理的答案](https://laravel-china.org/articles/9143/write-an-interview-and-share-my-answers)

[PHP 面试知识点汇总 ](https://github.com/eaglewu/php-interview-best-practices-in-china )

[平时积累 ](https://github.com/OMGZui/noteBook)

[PHP 代码简洁之道](https://github.com/ryanmcdermott/clean-code-javascript )

[PHP PSR 标准规范]( https://www.twle.cn/l/yufei/phppsr/php-psr-index.html)

 [psr](https://laravel-china.org/docs/psr )
 
[PHP 开发知识结构 ](https://github.com/han8gui/PHPer) 

[PHP多进程系列笔记](https://mp.weixin.qq.com/s/af2my0IC4VIo1WNaCvZAaA)

[Redis从入门到实践]( https://juejin.im/post/5a912b3f5188257a5c608729) 

[浅谈消息队列及常见的消息中间件](https://juejin.im/post/5b41fe36e51d45191252e79e)

[《程序员练级攻略》推荐必读书籍清单 ](https://time.geekbang.org/column/article/10793) 

[redis开发设计规范及案例分析](https://mp.weixin.qq.com/s/vS8IMgBIrfGpZYNUwtXrPQ )

[MySQL运维：索引与查询性能优化](https://juejin.im/entry/5b444bf05188251a8d36d034)

[从输入URL到页面展示到底发生了什么 ](https://juejin.im/entry/5b44155f6fb9a04f932fdf80)

[数据结构与算法](https://mp.weixin.qq.com/s/FslsYpofN5vE20TEfJNwrw)

[PHP面试：说说你理解的二叉树吧]( https://segmentfault.com/a/1190000015635928)

[初中级PHP面试基础汇总 ](https://segmentfault.com/a/1190000015412706)

 https://segmentfault.com/a/1190000010250591 
 
[php 经典排序算法（解析）]( https://segmentfault.com/a/1190000011751912)

[PHP面试之一：PHP基础知识点]( https://segmentfault.com/a/1190000011335262)

[PHPer、Laravel 面试可能会遇到的问题及答案](https://github.com/todayqq/caseInterviewQuestions )

[PHPer 面试指南-扩展阅读资源整理](https://segmentfault.com/a/1190000012971148)

[3年PHPer的面试总结]( http://coffeephp.com/articles/4)

[PHP 无限级分类最佳实践](https://segmentfault.com/a/1190000008265618)

[数据库面试题(开发者必看)]( https://segmentfault.com/a/1190000013517914)

[10个值得深思的PHP面试问题](https://segmentfault.com/a/1190000005032279)

[php 高并发](https://www.cnblogs.com/phpper/p/6716248.html)

[SegmentFault 技术周刊 Vol.31 - 码农也要学算法](https://segmentfault.com/a/1190000010600318) 

[SegmentFault 技术周刊 Vol.6 - 面试那些事儿](https://segmentfault.com/a/1190000006950447) 

[笔试面试](https://segmentfault.com/a/1190000012770931)

[PHP常见算法-面试篇 ](http://www.cnblogs.com/zswordsman/p/5824599.html)

[PHPer 面试指南-扩展阅读资源整理](https://segmentfault.com/a/1190000012971148)

[shell在手分析服务器日志不愁]( https://segmentfault.com/a/1190000009745139)

[PHPer 面试可能会遇到的问题](https://github.com/justcodingnobb/fuck-php-interview)

[程序员的自我修养](https://www.kancloud.cn/kancloud/a-programmer-prepares/78223)

[小土刀的面试刷题笔记](https://wdxtub.com/interview/14520847747820.html)

[笔试面试知识整理](https://github.com/HIT-Alibaba/interview)

[MySQL 避坑宝典](https://github.com/XiaoMi/soar/blob/master/doc/heuristic.md)
