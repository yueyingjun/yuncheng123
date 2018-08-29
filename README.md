# 如何将数据从前台(html)传到后台(python)

1. 首先安装 flask
    ```
    pip install Flask
    ```
2. 使用flask,创建一个文件，并且写入一下代码

    ```
    from flask import Flask,request
    app=Flask(__name__)
    @app.route("/api/photo",methods=["GET","POST"])
    def index():
        base=request.form["url"]
        print(base)
        return "ok111111111111"

    app.run("localhost",5000)
    ```

3. 运行该文件
   **pycharm 右键点击  run**

4. 运行vue
    1. 进入vue的工程目录
    2. 运行 npm run start
    3. 并且在浏览器里面打开 localhost:8080

5. 找到vue里面的 face.vue这个页面
    ```
    fetch("/api/photo",{
               method:"post",
               headers:{
                 "content-type":"application/x-www-form-urlencoded"
               },
               body:"url="+base+"&name="+this.name
             })

    ```

6. 开始运行

7. 安装numpy
    ```
    pip install numpy
    ```
8. 安装 cv2

    ```
    pip install opencv-python
    ```

9. 配置代理

   ```
   proxyTable: {  //代理的功能   npm run start  8080  falsk 5000
      '/api': {
            target: 'http://localhost:5000', // 接口的域名
            // secure: false,  // 如果是https接口，需要配置这个参数
            changeOrigin: true, // 如果接口跨域，需要进行这个参数配置
            pathRewrite: {
                '^/api': '/api'
            }
        }
    },
   ```





