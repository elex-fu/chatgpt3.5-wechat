# encoding:utf-8

import config
from channel import channel_factory
from common.log import logger
from concurrent.futures import ThreadPoolExecutor


if __name__ == '__main__':
    try:
        # load config
        config.load_config()
        
        # 微信聊天create channel
        channel2 = channel_factory.create_channel("wx")
        # # startup channel
        channel2.startup()
    except Exception as e:
        logger.error("App startup failed!")
        logger.exception(e)
