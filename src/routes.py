# coding:utf-8
import tornado
import tornado.ioloop
import tornado.web
import tornado.template
from src.controller import (search,demo,compare)

def getRoutes(config):
    Routes = [
        (r"/", demo.HomeHandler),
        (r"/demo", demo.DemoHandler),
        (r"/search", demo.DemoSearchHandler),
        (r"/search_color", demo.DemoSearchColorHandler),

        (r"/upload_search", demo.DemoUploadSearchHandler),
        (r"/upload_search_color", demo.DemoUploadSearchColorHandler),

        (r'/img/(.*)', tornado.web.StaticFileHandler, {'path': config.STATIC_DIR}),
        (r'/tests/(.*)', tornado.web.StaticFileHandler, {'path': config.PROJECT_DIR+"/tests/"}),
        # ---------------------------------------------
        (r'/_search/json/(.*)', search.JsonHandler),



        (r'/pc(.*)',compare.pcHandler),
        # (r'/pc/(.*)',compare.pcHandler),
        # (r'/color(.*)',compare.pcHandler),
        # (r'/index(.*)',compare.pcHandler),

        # 色彩接口 /color?path1=*
        # 推荐接口 /recommend?path1=*
        # 重建索引 /reindex?type=*

    ]

    return Routes