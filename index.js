import express from "express";
import fs from "fs";

const app = express();
//creo el objeto de mi app, y uso listen para escuchar:

const readData = ()=> {
    const data = fs.readFileSync("./Instalaciones_deportivas.json")
    console.log(JSON.parse(data))
}

readData();

app.get("/",(req,res)=>
{
    res.send("pruebaaaa")
})

app.listen(8080,()=> 
{
    console.log('servr¡er escucha en el puerto 8080')
});