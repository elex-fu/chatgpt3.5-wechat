# encoding:utf-8

import config
from channel import channel_factory
from common.log import logger
from concurrent.futures import ThreadPoolExecutor


if __name__ == '__main__':
    try:
        # load config
        config.load_config()
        
        # 微信公众号
        channel1 = channel_factory.create_channel("wxmp")
        # startup channel
        channel1.startup()

    except Exception as e:
        logger.error("App startup failed!")
        logger.exception(e)
