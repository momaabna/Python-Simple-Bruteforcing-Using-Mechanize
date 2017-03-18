<?php

$user = $_GET['user'];
$pass = $_GET['pass'];
$u ='admin';
$p ='1234';
if ($user==$u & $pass ==$p ){
echo 'Logged in SuccesFully ..';

}else{
echo 'failed to login';
}




?>
